import operator

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

from employee import order
from restaurant import models

# Create your views here.
from employee.employeeForms import OrderAuthenticationForm, CookDuty, RecipeForm, AbilityForm, FoodOfferForm, \
    MaterialForm, ReportForm, OrderingForm, WaiterDutyForm, DeliveryDutyForm
from restaurant.models import Order, ParkingInOrder, ChairInOrder, Food, FoodCook, Cook, FoodType, CookAbility, \
    FoodOffer, Material, Warehouse, MaterialInWarehouse, MaterialInFood, Waiter, DeliveryMan, OrderWaiter, \
    OrderDeliveryMan, Employee, FoodInMenu, MyUser



def hello(request):
    return HttpResponse(content='hello')


def search_order_by_id(id):
    all_orders = Order.objects.all()
    for order in all_orders:
        if order.trackID == id:
            return order

    pass


def search_parking_for_order(order):
    all_parkings = ParkingInOrder.objects.all()
    parkings = []
    for i in all_parkings:
        if i.order == order:
            parkings.append(i.parking)

    return parkings


def search_chair_for_order(order):
    all_chairs = ChairInOrder.objects.all()
    chairs = []
    for i in all_chairs:
        if i.order == order:
            chairs.append(i.chair)

    return chairs


def foods_in_order(order):
    res = []
    all_foods = Food.objects.all()
    for food in all_foods:
        if food.order == order:
            res.append(food)

    return res


def foods_for_cook(cook):
    ans = []
    all_tasks = FoodCook.objects.all()
    for task in all_tasks:
        if task.cook == cook:
            ans.append(task)
    return ans


def authentication_check(request):
    if request.method == 'POST':
        form = OrderAuthenticationForm(request.POST)
        if form.is_valid():
            result_order = search_order_by_id(form.cleaned_data['order_id'])
            chairs = search_chair_for_order(result_order)
            parkings = search_parking_for_order(result_order)
            foods = foods_in_order(result_order)
            if not result_order:
                result_order = 'null'
            context = {'form': form, 'order': result_order, 'chairs': chairs, 'parkings': parkings, 'foods': foods}
            return render(request, "employee/authenticate_order.html", context)

    else:
        form = OrderAuthenticationForm()

    return render(request, 'employee/authenticate_order.html', {'form': form, 'order': 'first'})
    pass


def clerk_authentication(request):
    if request.method == 'POST':
        form = OrderAuthenticationForm(request.POST)
        if form.is_valid():
            result_order = search_order_by_id(form.cleaned_data['order_id'])
            chairs = search_chair_for_order(result_order)
            parkings = search_parking_for_order(result_order)
            foods = foods_in_order(result_order)
            if not result_order:
                result_order = 'null'
            context = {'form': form, 'order': result_order, 'chairs': chairs, 'parkings': parkings, 'foods': foods}
            return render(request, "employee/clerck_authentication.html", context)

    else:
        form = OrderAuthenticationForm()

    return render(request, 'employee/clerck_authentication.html', {'form': form, 'order': 'first'})
    pass


def delivery_authentication(request):
    if request.method == 'POST':
        form = OrderAuthenticationForm(request.POST)
        if form.is_valid():
            result_order = search_order_by_id(form.cleaned_data['order_id'])
            chairs = search_chair_for_order(result_order)
            parkings = search_parking_for_order(result_order)
            foods = foods_in_order(result_order)
            if not result_order:
                result_order = 'null'
            context = {'form': form, 'order': result_order, 'chairs': chairs, 'parkings': parkings, 'foods': foods}
            return render(request, "employee/deliveryman_authentication.html", context)

    else:
        form = OrderAuthenticationForm()

    return render(request, 'employee/deliveryman_authentication.html', {'form': form, 'order': 'first'})
    pass


def waiter_authentication(request):
    if request.method == 'POST':
        form = OrderAuthenticationForm(request.POST)
        if form.is_valid():
            result_order = search_order_by_id(form.cleaned_data['order_id'])
            chairs = search_chair_for_order(result_order)
            parkings = search_parking_for_order(result_order)
            foods = foods_in_order(result_order)
            if not result_order:
                result_order = 'null'
            context = {'form': form, 'order': result_order, 'chairs': chairs, 'parkings': parkings, 'foods': foods}
            return render(request, "employee/waiter_authentication.html", context)

    else:
        form = OrderAuthenticationForm()

    return render(request, 'employee/waiter_authentication.html', {'form': form, 'order': 'first'})
    pass


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


def check_done_foods(picked):
    done = []
    for f in picked:
        all_task = FoodCook.objects.all()
        for task in all_task:
            if str(task.food.food_type.name) + ' برای سفارش ' + str(task.food.order.trackID) + ' : تعداد ' + str(
                    task.food.number) == f:
                done.append(task)
                print('saved')
    for d in done:
        order = d.food.order
        d.done = True
        finished = True
        d.save()
        for o in FoodCook.objects.all():
            if o.food.order == order and o.done == False:
                finished = False
        if finished:
            if order.place:
                delivery = choose_delivery()
                newObj = OrderDeliveryMan(deliveryman=delivery, order=order, done=False)
                newObj.save()
            else:
                waiter = choose_waiter()
                newObj = OrderWaiter(waiter=waiter, order=order, done=False)
                newObj.save()


def duty_list_cook(request):
    user = request.user.id
    userObj = User.objects.get(pk=user)
    myuser = MyUser.objects.get(user=userObj)
    emp = Employee.objects.get(user=myuser)
    c = emp.cook

    if request.method == 'POST':
        # c = Cook.objects.all()[0] #TODO
        form = CookDuty(cook=c, data=request.POST)
        if form.is_valid():
            print(form.cleaned_data['duty'].__len__())
            check_done_foods(form.cleaned_data['duty'])
            return render(request, 'employee/cook_duty.html', {'form': form})
    else:
        # c = Cook.objects.all()[0]
        form = CookDuty(cook=c)
    return render(request, 'employee/cook_duty.html', {'form': form})


def set_recipe_for_food(food_name, recipe):
    food = FoodType.objects.get(name=food_name)
    print('price')
    print(food.recipe)
    food.recipe = recipe
    food.save()


def set_material_in_food(request):
    for m in Material.objects.all():
        val = request.POST[m.name]
        if val != '':
            newObj = MaterialInFood()
            newObj.food = FoodType.objects.get(name=request.POST['food'])
            newObj.material = m
            newObj.value = int(val)
            newObj.save()


def set_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            set_recipe_for_food(request.POST['food'], form.cleaned_data['recipe'])
            set_material_in_food(request)
            context = {'form': form, 'materials': Material.objects.all(), 'foods': FoodType.objects.all()}
            return render(request, 'employee/set_recipe.html', context)

    else:
        form = RecipeForm()
        context = {'form': form, 'materials': Material.objects.all(), 'foods': FoodType.objects.all()}
    return render(request, 'employee/set_recipe.html', context)


def add_cook_ability(food_name, num, c):
    food = FoodType.objects.get(name=food_name)
    ability = CookAbility(ability=food, number=num, cook=c)
    ability.save()

    pass


def add_ability(request):
    if request.method == 'POST':
        form = AbilityForm(data=request.POST)
        if form.is_valid():
            user = request.user.id
            userObj = User.objects.get(pk=user)
            myuser = MyUser.objects.get(user=userObj)
            emp = Employee.objects.get(user=myuser)
            c = emp.cook
            # c = Cook.objects.all()[0]
            add_cook_ability(form.cleaned_data["foods"], form.cleaned_data['number'], c)
            return render(request, 'employee/add_ability.html', {'form': form})
    else:
        form = AbilityForm()
    return render(request, 'employee/add_ability.html', {'form': form})


def add_food_offer(food_name, suggest_name):
    all_foods = FoodType.objects.all()
    for f in all_foods:
        if f.name == food_name:
            food = f
        if f.name == suggest_name:
            suggest = f
    offer = FoodOffer(food=food, offer=suggest)
    offer.save()


def set_food_offer(request):
    if request.method == 'POST':
        form = FoodOfferForm(data=request.POST)
        if form.is_valid():
            add_food_offer(form.cleaned_data['food'], form.cleaned_data['suggest'])
            return render(request, 'employee/food_offer.html', {'form': form})
    else:
        form = FoodOfferForm()
    return render(request, 'employee/food_offer.html', {'form': form})


def add_material_to_warehouse(m_name, w_id, val, date):
    material = Material.objects.get(name=m_name)

    for w in Warehouse.objects.all():
        if "انبار شماره " + str(w.warehouse_id) == w_id:
            warehouse = w

    newObj = MaterialInWarehouse(material=material, warehouse=warehouse, value=val, expire_date=date)
    newObj.save()


def add_material(request):
    if request.method == 'POST':
        form = MaterialForm(data=request.POST)
        if form.is_valid():
            add_material_to_warehouse(form.cleaned_data['material'], form.cleaned_data['wareHouse'],
                                      form.cleaned_data['value'], form.cleaned_data['expire_date'])
            return render(request, 'employee/add_material.html', {'form': form})
    else:
        form = MaterialForm()
    return render(request, 'employee/add_material.html', {'form': form})


def get_report_of_warehouse_by_id(w_in):
    all_data = MaterialInWarehouse.objects.all()
    ans = []
    for d in all_data:
        if "انبار شماره " + str(d.warehouse.warehouse_id) == w_in:
            ans.append(d)

    return ans


def get_address(w):
    all_data = Warehouse.objects.all()
    ans = ''
    for d in all_data:
        if "انبار شماره " + str(d.warehouse_id) == w:
            ans = d.address

    return ans


def get_warehouse_report(request):
    if request.method == 'POST':
        form = ReportForm(data=request.POST)
        if form.is_valid():
            result = get_report_of_warehouse_by_id(form.cleaned_data['warehouse'])
            print(form.cleaned_data['warehouse'])
            if result == []:
                result = 'null'
            address = get_address(form.cleaned_data['warehouse'])
            return render(request, 'employee/warehouse_report.html',
                          {'form': form, 'result': result, 'address': address})
    else:
        form = ReportForm()
    return render(request, 'employee/warehouse_report.html', {'form': form, 'result': 'first'})


#     if val != '':






def get_foods_in_branch(branch):
    ans = []
    for f in FoodType.objects.all():
        if FoodInMenu.objects.filter(food_type=f , menu=branch.menu).count()>0 :
            ans.append(f)
    return ans


def get_order(request):
    user = request.user.id
    userObj = User.objects.get(pk=user)
    myuser = MyUser.objects.get(user=userObj)
    emp = Employee.objects.get(user=myuser)
    clerk = emp.clerk
    branch = emp.branch
    foods = get_foods_in_branch(branch)
    if request.method == 'POST':

        form = OrderingForm(data=request.POST)
        if form.is_valid():
            order.submit_order(request)
            return render(request, 'employee/employee_order.html',
                          {'form': form, 'foods': foods})
    else:
        form = OrderingForm()
    return render(request, 'employee/employee_order.html', {'form': form, 'foods': foods})


def check_done_waiter_duty(picked):
    done = []
    for f in picked:
        all_task = OrderWaiter.objects.all()
        for task in all_task:
            if 'سفارش شماره‌ی : ' + str(task.order.trackID) == f:
                done.append(task)
                print('saved')
    for d in done:
        d.done = True
        d.save()
        o = d.order
        o.is_done = True
        o.save()


def duty_list_waiter(request):
    user = request.user.id
    userObj = User.objects.get(pk=user)
    myuser = MyUser.objects.get(user=userObj)
    emp = Employee.objects.get(user=myuser)
    w = emp.waiter
    if request.method == 'POST':

        form = WaiterDutyForm(waiter=w, data=request.POST)
        if form.is_valid():
            print(form.cleaned_data['duty'].__len__())
            check_done_waiter_duty(form.cleaned_data['duty'])
            return render(request, 'employee/waiter_duty.html', {'form': form})
    else:

        form = WaiterDutyForm(waiter=w)
    return render(request, 'employee/waiter_duty.html', {'form': form})


def check_done_delivery_duty(picked):
    done = []
    for f in picked:
        all_task = OrderDeliveryMan.objects.all()
        for task in all_task:
            if 'سفارش شماره‌ي : ' + str(task.order.trackID) == f:
                done.append(task)
                print('saved')
    for d in done:
        d.done = True
        d.save()
        o = d.order
        o.is_done = True
        o.save()


def duty_list_deliveryman(request):
    user = request.user.id
    userObj = User.objects.get(pk=user)
    myuser = MyUser.objects.get(user=userObj)
    emp = Employee.objects.get(user=myuser)
    d = emp.deliveryman
    if request.method == 'POST':

        form = DeliveryDutyForm(deliveryman=d, data=request.POST)
        if form.is_valid():
            print(form.cleaned_data['duty'].__len__())
            check_done_delivery_duty(form.cleaned_data['duty'])
            return render(request, 'employee/deliveryman_duty.html', {'form': form})
    else:

        form = DeliveryDutyForm(deliveryman=d)
    return render(request, 'employee/deliveryman_duty.html', {'form': form})
