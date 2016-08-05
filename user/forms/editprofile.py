from django import  forms
from restaurant.models import User


class EditProfileForm(forms.ModelForm):
    # first_name = forms.CharField(label='First Name')
    # last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
