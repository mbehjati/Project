from django import forms
from .models import TasteType, Menu


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class SearchForm(forms.Form):
    CHOICES = (('1', 'First',), ('2', 'Second',))
    one_to_ten = ()

    for i in range(1, 10):
        one_to_ten += ((i, str(i)),)

    all_tastes = TasteType.objects.all()
    tastes = ()
    for t in all_tastes:
        tastes += ((t, t.name),)

    all_types = Menu.objects.all()
    types = ()
    for t in all_types:
        types += ((t, t.name),)

    name = forms.CharField(max_length=50)
    type = forms.ChoiceField(label='type', widget=forms.Select, choices=types)
    score_from = forms.ChoiceField(widget=forms.Select, choices=one_to_ten)
    score_to = forms.ChoiceField(widget=forms.Select, choices=one_to_ten)
    taste = forms.ChoiceField(label='taste', widget=forms.Select, choices=tastes)
    price_from = forms.IntegerField()
    price_to = forms.IntegerField()
