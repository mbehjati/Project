from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template import loader
from .models import *

def index(request):
    return render(request, 'restaurant/home.html')

def branch(request):
    branches = Branch.objects.all()
    return render(request, 'restaurant/branch.html', {'branches':branches})

def menu(request):
    foods = FoodType.objects.all()
    return render(request, 'restaurant/menu.html', {'menu' : foods})

# def food(request, food_name):


from .forms import NameForm , SearchForm
from restaurant.models import FoodType
from .forms import NameForm, SearchForm



def search_in_foods(form):
    result = {}
    all_foods = FoodType.objects.all()
    if form.is_valid():
        for food in all_foods:
            if food.name.__contains__(form.cleaned_data['name']) and food.price <= form.cleaned_data['price_to']:
                if food.price >= form.cleaned_data['price_from']:
                    result[str(food.name)] = food
    return result
    pass


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            result = search_in_foods(form)
            # redirect to a new URL:
            context = {'result': result, 'form': form}
            return render(request, "restaurant/search.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'restaurant/search.html', {'form': form})
