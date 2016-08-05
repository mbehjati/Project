from django import forms
from restaurant.models import MyUser
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    pass_conf = forms.CharField(widget=forms.widgets.PasswordInput, label="Password(again)")

    class Meta:
        model = User
        fields = ['username', 'password', 'pass_conf', 'first_name', 'last_name', 'email']
        widgets = {
            'password': forms.PasswordInput,
        }


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        exclude = ['user']


# class RegisterForm(forms.ModelForm):
#     password2 = forms.CharField(widget=forms.widgets.PasswordInput, label="Password(again)")
#
#     class Meta:
#         model = MyUser
#         fields = ['username', 'password', 'password2', 'name', 'address', 'phone_number', 'email']
#         widgets = {
#             'password': forms.PasswordInput,
#         }


'''class RegisterForm(forms.ModelForm):
    pass_conf = forms.CharField(max_length=50, label="password(again)", widget=forms.PasswordInput)
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    password = forms.CharField(max_length=50, label="password", widget=forms.PasswordInput)
    email = forms.EmailField()
    # isHotelier = forms.BooleanField(label="ثبت نام به عنوان هتل دار", required=False)
    # captcha = CaptchaField()

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        _password = cleaned_data.get('password')
        _pass_conf = cleaned_data.get('pass_conf')

        if _pass_conf and _password and _pass_conf != _password:
            print("validation error")
            raise forms.ValidationError('تکرار کلمه عبور نادرست است.')
        return cleaned_data

    class Meta:
        model = MyUser
        fields = ['username', 'password', 'pass_conf', 'first_name', 'last_name', 'phone_number', 'email']
        # fields = ['username', 'password', 'pass_conf', 'first_name', 'phone_number']
        widgets = {
            'password': forms.PasswordInput,
        }

    # def save(self, **kwargs):
    #     myuser = super().save(commit=False)
    #     user = User.objects.create(username=self.cleaned_data['username'], first_name=self.cleaned_data['first_name'],)
    #     user.set_password(self.cleaned_data['password'])
    #     myuser.user = user
    #     myuser.phone_number = self.cleaned_data['phone_number']
    #     myuser.save(commit=True)
'''

'''
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Entered passwords don't match. Retry entering them.")
        return cleaned_data

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        if commit:
            user.save()
        return user
'''