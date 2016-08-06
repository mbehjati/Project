from django.shortcuts import render, redirect
from user.forms import RegisterForm, LoginForm
from django.contrib.auth import login as django_login, logout as django_logout,authenticate
from django.http.response import HttpResponseRedirect
# from restaurant.models import MyUser
# from restaurant.models import User, Employee
# from django.contrib.auth.decorators import login_required

'''
# @login_required(login_url='/user/login/')
def view_profile(request):
    user_id = request.user.id
    try:
        user = User.objects.get(pk=user_id)
        return render(request, 'user/profile_user.html', {'user': user})

    except User.DoesNotExist:
        # try:
        #     employee = Employee.objects.get(pk=user_id)
        #     return render(request, 'user/profile_employee.html', {'employee': employee})
        # except employee.DoesNotExist:
        redirect("/")
'''

'''
def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            # TODO: say to manager to activate account
            return redirect("user/regOK.html")
    else:
        form = RegisterForm()
    return render(request, "user/register.html", {'form': form})
'''

'''
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['pass_conf']
            # if form.cleaned_data['isHotelier']:
            #     del form.cleaned_data['isHotelier']
            #     user = Hotelier(**(form.cleaned_data))
            #     user.set_password(form.cleaned_data['password'])
            #     user.save()
            # else:
            #     del form.cleaned_data['isHotelier']
            user = MyUser(form.cleaned_data)
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()
            # send_activation_link(user)
        return render(request, 'user/regOK.html')
    else:
        form = RegisterForm()
    return render(request, "user/register.html", {'form': form})
'''
'''
def login(request):
    # if not request.user.is_anonymous:
    #     django_logout(request)
    # redirect_to = request.REQUEST.get('next', '')
    # if not redirect_to:
    #     redirect_to = "/simorgh/home/"
    #
    #
    # # forgetForm = ForgotForm()
    # message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                my_user = MyUser.objects.get(pk=user.id)
                if my_user.active:
                    django_login(request, user)
                    return HttpResponseRedirect("/regOK.html")
                else:
                    form = LoginForm()
                    # message = "حساب شما غیر فعال است."
            else:
                form = LoginForm()
                # message = "نام کاربری یا گذرواژه شما اشتباه است."
    else:
        form = LoginForm()
    return render(request, "user/login.html", {'form': form})
'''

'''
def login(request):
    if request.POST:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = form.login(request)
            if user:
                django_login(request, user)
                return HttpResponseRedirect("/regOK.html")
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})
'''


def logout(request):
    django_logout(request)
    return redirect('/')
