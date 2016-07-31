
from django import forms
class OrderAuthenticationForm(forms.Form):
    order_id = forms.IntegerField()
