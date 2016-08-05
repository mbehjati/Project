from django import  forms
from restaurant.models import User


class EditUserNameForm(forms.ModelForm):
    # first_name = forms.CharField(label='First Name')
    # last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ['username']
