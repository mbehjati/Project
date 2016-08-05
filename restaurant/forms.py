from django import forms
from django.forms import ModelForm
from material import  *
from .models import *


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class SearchForm( forms.Form):
    # layout = Layout(Row('name'))
    CHOICES = (('1', 'First',), ('2', 'Second',))
    one_to_ten = ()

    for i in range(1, 10):
        one_to_ten += ((i, str(i)),)

    all_tastes = TasteType.objects.all()
    tastes = (('همه' ,'همه' ),)
    for t in all_tastes:
        tastes += ((t,t.name),)

    all_types = Menu.objects.all()
    types =  (('همه' ,'همه' ),)
    for t in all_types:
        types += ((t, t.name),)

    name = forms.CharField(max_length=50 , required=False,label='اسم')
    type = forms.ChoiceField( widget=forms.Select, choices=types , required=False,label='نوع')
    score_from = forms.ChoiceField(widget=forms.Select, choices=one_to_ten , required=False ,label='امتیاز از')
    score_to = forms.ChoiceField(widget=forms.Select, choices=one_to_ten , required=False,label='امتیاز تا')
    taste = forms.ChoiceField(widget=forms.Select, choices=tastes , required=False,label='طعم')
    price_from = forms.IntegerField(required=False, label='قیمت از')
    price_to = forms.IntegerField(required=False,label='قیمت تا')

    layout = Layout('name', Row('taste','type'),Row('score_to','score_from'),Row('price_to','price_from'))



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [  'branch','place']
        widgets={'place':forms.RadioSelect}
        labels = {
            'place': 'شیوه تحویل'
        }