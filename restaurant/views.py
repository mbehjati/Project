import json
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.forms import Form
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from employee.order import submit_order, submit_order_customer, calculate_price
from restaurant.models import FoodType
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404, render
from employee import order


def index(request):
    return render(request, 'restaurant/home.html')


def branch(request):
    branches = Branch.objects.all()
    return render(request, 'restaurant/branch.html', {'branches': branches})


def menu(request):
    foods = FoodType.objects.all()
    return render(request, 'restaurant/menu.html', {'menu': foods})


# def food(request, food_name):

def food(request, food_name):
    print('here')
    print(food_name)
    food_type = get_object_or_404(FoodType, pk=food_name)
    # return HttpResponse('inja')
    return render(request, 'restaurant/food.html', {'food': food_type})


from .forms import NameForm, SearchForm
from restaurant.models import FoodType
from .forms import NameForm, SearchForm


def order(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        salam = request.POST.get('branch', '')
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            branch = form.cleaned_data['branch']
            menuinbranch = branch.menu_set.all()
            # Order.objects.get().
            # redirect to a new URL:
            return HttpResponse(salam)
            # return render(request, "restaurant/search.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderForm()

    return render(request, 'restaurant/order.html', {'form': form})


def food_is_type(food, t):
    type = Menu.objects.get(name=t)
    # obj = FoodInMenu.objects.get(food_type=food , menu=type)
    if FoodInMenu.objects.filter(food_type=food, menu=type).count() > 0:
        return True
    return False


def food_has_taste(f, t):
    taste = TasteType.objects.get(name=t)
    # obj = FoodInMenu.objects.get(food_type=food , menu=type)
    if FoodTypeTaste.objects.filter(food=f, taste=taste).count() > 0:
        return True
    return False


def search_in_foods(form):
    all_foods = FoodType.objects.all()
    result = []
    for f in all_foods:
        result.append(f)
    print(result)
    if form.is_valid():
        if form.cleaned_data['name']:
            for food in list(result):
                print(str(food))
                if not food.name.__contains__(form.cleaned_data['name']):
                    result.remove(food)
                    print(str(food) + "delete1")
        if form.cleaned_data['type'] != 'همه':
            for food in list(result):
                print(str(food))
                if not food_is_type(food, form.cleaned_data['type']):
                    result.remove(food)
                    print(str(food) + "delete2")
        if form.cleaned_data['score_from']:
            for food in list(result):
                if not food.rate >= int(form.cleaned_data['score_from']):
                    result.remove(food)
                    print(str(food) + "delete3")
        if form.cleaned_data['score_to']:
            for food in list(result):
                if not food.rate <= int(form.cleaned_data['score_to']):
                    result.remove(food)
                    print(str(food) + "delete4")
        if form.cleaned_data['price_from']:
            for food in list(result):
                if not food.price >= int(form.cleaned_data['price_from']):
                    result.remove(food)
                    print(str(food) + "delete5")
        if form.cleaned_data['price_to']:
            for food in list(result):
                if not food.price <= int(form.cleaned_data['price_to']):
                    result.remove(food)
                    print(str(food) + "delete6")

        if form.cleaned_data['taste'] != 'همه':
            for food in list(result):
                if not food_has_taste(food, form.cleaned_data['taste']):
                    result.remove(food)
                    print(str(food) + "delete7")

    return result
    pass


def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            result = search_in_foods(form)
            # redirect to a new URL:
            print(result)
            context = {'result': result, 'form': form}
            return render(request, "restaurant/search.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'restaurant/search.html', {'form': form})

@login_required
def show_branch_menu(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    user = request.user.id
    user_obj = User.objects.get(pk=user)
    myuser = MyUser.objects.get(user=user_obj)
    menu = branch.menu.foodinmenu_set.values_list('food_type', flat=True)
    a = []
    for f in menu:
        obj = get_object_or_404(FoodType, pk=f)
        a.append(obj)
    if request.method == 'POST':
        # order = Order(is_changable=True, is_permanent=False, has_child=False, branch_id = branch_id, place=True, trackID=1)
        ord = Order()
        food_dict = {}
        for foodt in a:
            esm = foodt.name
            number = request.POST[esm]
            if(number > 0):
                food_dict[foodt] = number

        date = request.POST['date']
        time = request.POST['time']
        submit_order_customer(myuser, branch , date , time , food_dict)
        # TODO: redirect to correct page
        return HttpResponse("bia berim dasht")
    else:
        dic = []
        for foodo in menu:
            off = FoodOffer.objects.filter(food=foodo).values_list('offer', flat=True)
            dic.append((foodo, off))
        print(dic)
    return render(request, 'restaurant/branchm.html', {'menu': a, 'branch_id': branch_id, 'dic': dic})


@csrf_exempt
def costumer(request):
    orders = Order.objects.all()
    prices={}
    for ord in orders:
        prices[ord]  = calculate_price(ord)

    if (request.method == 'POST'):
        print('salam')
        print(request.POST['name'])
        #TODO: remove from database
        return HttpResponse('successfully deleted')
    #TODO: done orders
    return render(request, 'restaurant/costumer_order.html', {'orders': orders , 'prices':prices})


def order_detail(request, order_id):
    requested_order = get_object_or_404(Order, pk=order_id)
    order_food = []
    food_sets = Food.objects.filter(order_id=order_id)
    for food in food_sets:
        foodt = get_object_or_404(FoodType, pk=food.food_type)
        order_food.append((foodt, food.number, foodt.price * food.number))

        # = requested_order.food_set.values_list('food_type','number')
    # print(order_food)
    return render(request, 'restaurant/order_detail.html', {'order': requested_order, 'order_food': order_food})


def comment(request, order_id):
    requested_order = get_object_or_404(Order, pk=order_id)
    foods = requested_order.food_set.values_list('food_type', flat=True)
    delivery = requested_order.orderdeliveryman_set.values_list('deliveryman', flat=True)
    waiters = requested_order.orderwaiter_set.values_list('waiter', flat=True)
    if (request.method == 'POST'):
        result = request.POST
        user = request.user.id
        user_obj = User.objects.get(pk=user)
        myuser = MyUser.objects.get(user=user_obj)
        for food in foods:
            if not result[food + "-comment"] == "":
                new_comment = Comment(text=result[food + "-comment"],
                                      state=False,
                                      date=datetime.now(),
                                      user=myuser,
                                      food=food)
                new_comment.save()
            if not result[food + "-rate"] == "":
                len = Comment.objects.filter(food=food).__len__()
                rate = FoodType.objects.filter(pk=food)[0].rate
                rate = (rate * (len - 1) + int(result[food + "-rate"])) / len;

        for waiter in waiters:
            if not result[waiter + "-comment"] == "":
                new_comment = CommentEmp(text=result[food + "-comment"],
                                      state=False,
                                      date=datetime.now(),
                                      user=myuser,
                                      employee=waiter)
                new_comment.save()
            #     TODO: sare kari nabash
            # if not result[waiter + "-rate"] == "":
            #     len = Comment.objects.filter(food=food).__len__()
            #     rate = FoodType.objects.filter(pk=food)[0].rate
            #     rate = (rate * (len - 1) + int(result[food + "-rate"])) / len;
        for deli in delivery:
            if not result[deli + "-comment"] == "":
                new_comment = CommentEmp(text=result[deli + "-comment"],
                                      state=False,
                                      date=datetime.now(),
                                      user=myuser,
                                      employee=deli)
                new_comment.save()
            # if not result[food + "-rate"] == "":
            #     len = Comment.objects.filter(food=food).__len__()
            #     rate = FoodType.objects.filter(pk=food)[0].rate
            #     rate = (rate * (len - 1) + int(result[food + "-rate"])) / len;
        # TODO: redirect
        return HttpResponse("ثبت شد")

    return render(request, 'restaurant/order_comment.html',
                  {'order': requested_order, 'foods': foods, 'delivery': delivery, 'waiters': waiters})


def profile(request):
    # user = request.user.id
    # user_obj = User.objects.get(pk=user)
    # myuser = MyUser.objects.get(user=user_obj)
    return render(request, 'restaurant/profile.html')