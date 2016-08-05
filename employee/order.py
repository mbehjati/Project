import operator
import uuid

import datetime

from django.contrib.auth.models import User
from django.core.mail import send_mail

from restaurant.models import Branch, Order, FoodType, Food, Cook, CookAbility, DeliveryMan, OrderDeliveryMan, Employee, \
    Waiter, OrderWaiter, FoodCook, MyUser, Setting


def choose_cook(cooks):
    dic = {}
    for cook in cooks:
        dic[cook.cook_id.employee_id] = 0
    for order in FoodCook.objects.all():
        if order.done is False:
            dic[order.cook.cook_id.employee_id] += order.food.number
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
    emp = Employee.objects.get(employee_id=sorted_dic[0][0])
    return Cook.objects.get(cook_id=emp)


def choose_delivery():
    dic = {}
    for delivery in DeliveryMan.objects.all():
        dic[delivery.delivery_man_id.employee_id] = 0
    for order in OrderDeliveryMan.objects.all():
        if order.done is False:
            dic[order.delivery.delivery_man_id.employee_id] += 1
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
    emp = Employee.objects.get(employee_id=sorted_dic[0][0])
    return DeliveryMan.objects.get(delivery_man_id=emp)


def choose_waiter():
    dic = {}
    for waiter in Waiter.objects.all():
        dic[str(waiter.waiter_id.employee_id)] = 0
    for order in OrderWaiter.objects.all():
        if order.done is False:
            dic[str(order.waiter.waiter_id.employee_id)] += 1

    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))

    emp = Employee.objects.get(employee_id=sorted_dic[0][0])
    return Waiter.objects.get(waiter_id=emp)


def submit_order(request):
    trackID = int(uuid.uuid4().time_low) + int(uuid.uuid4().time_mid)
    user = request.user.id
    userObj = User.objects.get(pk=user)
    myuser = MyUser.objects.get(user=userObj)
    emp = Employee.objects.get(user=myuser)
    branch = emp.branch  # TODO real branch
    is_permanent = True
    is_changable = False
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    has_place = False
    order = Order(trackID=trackID, is_changable=is_changable, is_permanent=is_permanent, branch=branch, date=date, time=
    time, place=has_place)
    order.save()

    foods_order = []
    for f_type in FoodType.objects.all():
        val = request.POST[f_type.name]
        if val != '' and val != 0:
            food = Food(food_type=f_type, order=order, number=val, status=False)
            food.save()
            foods_order.append(food)

    for food in foods_order:
        cooks = []
        for c in CookAbility.objects.all():
            if c.ability == food.food_type:
                cooks.append(c.cook)
        cook = choose_cook(cooks)
        foodcook = FoodCook(cook=cook, food=food, done=False)
        foodcook.save()


def submit_order_customer(user, branch, date, time, dic, has_child):
    trackID = int(uuid.uuid4().time_low) + int(uuid.uuid4().time_mid)
    # branch = Branch.objects.all()[0]  # TODO real branch
    # is_permanent = True
    # is_changable = False
    # date = datetime.datetime.now().date()
    # time = datetime.datetime.now().time()
    has_place = True
    order = Order(trackID=trackID, is_changable=True, is_permanent=False, branch=branch, date=date, time=
    time, place=has_place, has_child=has_child, user=user)
    order.save()

    for food, val in dic:
        food = Food(food_type=FoodType.objects.get(name=food), order=order, number=val, status=False)
        food.save()


def confirm_order(order):
    order.is_permanent = True
    order.is_changable = False
    order.save()

    foods_order = []
    for f in Food.objects.all():
        if f.order == order:
            foods_order.append(f)

    for food in foods_order:
        cooks = []
        for c in CookAbility.objects.all():
            if c.ability == food.food_type:
                cooks.append(c.cook)
        cook = choose_cook(cooks)
        foodcook = FoodCook(cook=cook, food=food, done=False)
        foodcook.save()


def calculate_price(order):
    price = 0
    for food in Food.objects.all():
        if food.order == order:
            price += food.food_type.price
    return price


def send_mail_to_delivery(email, order):
    mail_list = []
    mail_list.append(email)
    mail_text = "سلام \nلطفا سفارش به شماره\u200Cی {0} را به آدرس زیر تحویل دهید:\n{1}".format(str(order.trackID), str(
        order.user.address))
    send_mail(str("وظیفه جدید"), mail_text, 'onlinefoodforyou@gmail.com',
              mail_list, fail_silently=False)


def send_mail_to_waiter(email, order):
    mail_list = []
    mail_list.append(email)
    mail_text = "سلام " + "\n" + "لطفا سفارش به شماره‌ی " + str(order.trackID) + " را تحویل دهید."
    send_mail(str("وظیفه جدید"), mail_text, 'onlinefoodforyou@gmail.com',
              mail_list, fail_silently=False)


def food_suggest():
    setting = Setting.objects.all()[0]
    if setting.most_liked:
        print('here')
        ordered_food = FoodType.objects.order_by('-rate')[:4]
        print('here2')
    elif setting.last_orders:
        last_foods = []
        for o in Order.objects.order_by('-date'):
            for f in Food.objects.all():
                if f.order == o :
                    last_foods.append(f)
        ordered_food = []
        number = 0
        for f in last_foods:
            if not f.food_type in ordered_food and number<4:
                ordered_food.append(f.food_type)
                number +=1

    print(ordered_food)


def chef_suggest(request):
    ans = []
    for c in Cook.objects.all():
        number = 0
        chef_food = None
        for ability in CookAbility.objects.all():
            if ability.cook == c and ability.number>number:
                chef_food = ability.ability
                number = ability.number
        if chef_food!=None:
            ans.append(chef_food)
    print(ans)
    return ans
