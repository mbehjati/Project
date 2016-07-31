from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse
from restaurant import models

# Create your views here.
from employee.employeeForms import OrderAuthenticationForm
from restaurant.models import Order, ParkingInOrder, ChairInOrder


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


def authentication_check(request):
    if request.method == 'POST':
        form = OrderAuthenticationForm(request.POST)
        if form.is_valid():
            result_order = search_order_by_id(form.cleaned_data['order_id'])
            chairs = search_chair_for_order(result_order)
            parkings = search_parking_for_order(result_order)
            context = {'form': form, 'order': result_order, 'chairs': chairs, 'parkings': parkings}
            return render(request, "employee/authenticate_order.html", context)

    else:
        form = OrderAuthenticationForm()

    return render(request, 'employee/authenticate_order.html', {'form': form})
    pass
