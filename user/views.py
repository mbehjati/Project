# from django.shortcuts import render, redirect
# from user.forms import RegisterForm, LoginForm
# from django.contrib.auth import login as django_login, logout as django_logout,authenticate
# from django.http.response import HttpResponseRedirect
# # from restaurant.models import MyUser
# # from restaurant.models import User, Employee
# # from django.contrib.auth.decorators import login_required
#
# '''
# # @login_required(login_url='/user/login/')
# def view_profile(request):
#     user_id = request.user.id
#     try:
#         user = User.objects.get(pk=user_id)
#         return render(request, 'user/profile_user.html', {'user': user})
#
#     except User.DoesNotExist:
#         # try:
#         #     employee = Employee.objects.get(pk=user_id)
#         #     return render(request, 'user/profile_employee.html', {'employee': employee})
#         # except employee.DoesNotExist:
#         redirect("/")
# '''
#
# '''
# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             # TODO: say to manager to activate account
#             return redirect("user/regOK.html")
#     else:
#         form = RegisterForm()
#     return render(request, "user/register.html", {'form': form})
# '''
#
# '''
# def register(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             del form.cleaned_data['pass_conf']
#             # if form.cleaned_data['isHotelier']:
#             #     del form.cleaned_data['isHotelier']
#             #     user = Hotelier(**(form.cleaned_data))
#             #     user.set_password(form.cleaned_data['password'])
#             #     user.save()
#             # else:
#             #     del form.cleaned_data['isHotelier']
#             user = MyUser(form.cleaned_data)
#             user.set_password(form.cleaned_data['password'])
#             user.is_active = True
#             user.save()
#             # send_activation_link(user)
#         return render(request, 'user/regOK.html')
#     else:
#         form = RegisterForm()
#     return render(request, "user/register.html", {'form': form})
# '''
# '''
# def login(request):
#     # if not request.user.is_anonymous:
#     #     django_logout(request)
#     # redirect_to = request.REQUEST.get('next', '')
#     # if not redirect_to:
#     #     redirect_to = "/simorgh/home/"
#     #
#     #
#     # # forgetForm = ForgotForm()
#     # message = ""
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 my_user = MyUser.objects.get(pk=user.id)
#                 if my_user.active:
#                     django_login(request, user)
#                     return HttpResponseRedirect("/regOK.html")
#                 else:
#                     form = LoginForm()
#                     # message = "حساب شما غیر فعال است."
#             else:
#                 form = LoginForm()
#                 # message = "نام کاربری یا گذرواژه شما اشتباه است."
#     else:
#         form = LoginForm()
#     return render(request, "user/login.html", {'form': form})
# '''
#
# '''
# def login(request):
#     if request.POST:
#         form = LoginForm(request.POST or None)
#         if form.is_valid():
#             user = form.login(request)
#             if user:
#                 django_login(request, user)
#                 return HttpResponseRedirect("/regOK.html")
#     else:
#         form = LoginForm()
#     return render(request, 'user/login.html', {'form': form})
# '''
#
#
# def logout(request):
#     django_logout(request)
#     return redirect('/')

from django.shortcuts import render, redirect
# from user.forms import RegisterForm, LoginForm
from user.forms import UserForm, MyUserForm, LoginForm, EditProfileForm, EditUserNameForm, EditPasswordForm
from django.contrib.auth import login as django_login, logout as django_logout ,authenticate
from django.http.response import HttpResponseRedirect
from restaurant.models import MyUser
from django.contrib.auth.models import User
# from restaurant.models import User, Employee
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm


def reset_confirm(request, uidb36=None, token=None):
    return password_reset_confirm(request, template_name='user/password_reset_confirm.html',
                                  uidb36=uidb36, token=token, post_reset_redirect=reverse('user/login.html'))


def reset(request):
    return password_reset(request, template_name='user/reset.html',
                          email_template_name='user/password_reset_form.html',
                          subject_template_name='user/reset_subject.txt',
                          post_reset_redirect=reverse('user/login.html'))


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

'''def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # u = User(name=request.POST.get('user'))
        if form.is_valid():
            del form.cleaned_data['pass_conf']
            # if form.cleaned_data['isHotelier']:
            #     del form.cleaned_data['isHotelier']
            #     user = Hotelier(**(form.cleaned_data))
            #     user.set_password(form.cleaned_data['password'])
            #     user.save()
            # else:
            #     del form.cleaned_data['isHotelier']
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'],
                                       first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],
                                       email=form.cleaned_data['email'])
            user.is_active = False
            user.save()
            myuser = MyUser.objects.create(phone_number=form.cleaned_data['phone_number'])
            myuser.user = user
            myuser.save()
            # user = uf.save()
            # userprofile = upf.save(commit=False)
            # userprofile.user = user
            # userprofile.save()
            # myuser.user = user
            # user.set_password(form.cleaned_data['password'])
            # myuser.is_active = False
            # user.is_active = True
            # user.save()
            # myuser.save()
            # send_activation_link(user)
        return render(request, 'user/regOK.html')
    else:
        form = RegisterForm()
    return render(request, "user/register.html", {'form': form})
'''


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = MyUserForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = User.objects.create_user(username=uf.cleaned_data['username'], password=uf.cleaned_data['password'],
                                            first_name=uf.cleaned_data['first_name'], last_name=uf.cleaned_data['last_name'],
                                            email=uf.cleaned_data['email'])
            user.save()
            # userprofile = User.objects.get(id=user.id).myuser



        #     userprofile = user.userprofile
        # except UserProfile.DoesNotExist, e:
        # userprofile = UserProfile(user=user)
        # userprofile.save()

            # userprofile = upf.save(commit=False)
            # userprofile.user = user

            userprofile = MyUser(user=user, phone_number=upf.cleaned_data['phone_number'])
            # userprofile.user.id = request.user.id
            userprofile.save()
            return render(request, 'user/regOK.html')
    else:
        uf = UserForm(prefix='user')
        upf = MyUserForm(prefix='userprofile')
    return render(request, 'user/register.html', {'userform': uf, 'userprofileform':upf})



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
                findeduser = User.objects.get(pk=user.id)
                # my_user = MyUser.objects.get(user=findeduser)
                if findeduser.is_active:
                    if findeduser.is_staff:
                        django_login(request, user)
                        return HttpResponseRedirect("user/regOK1.html")
                    else:
                        django_login(request, user)
                        return HttpResponseRedirect("user/regOK.html")
                else:
                    form = LoginForm()
                    print("account deactive")
                #     # message = "حساب شما غیر فعال است."
            else:
                form = LoginForm()
                print("pass or username wrong")
                # message = "نام کاربری یا گذرواژه شما اشتباه است."
    else:
        form = LoginForm()
    return render(request, "user/login.html", {'form': form})


@login_required(login_url='/user/login/')
def view_profile(request):
    user_id = request.user.id
    try:
        user1 = User.objects.get(pk=user_id)
        myuser=MyUser.objects.get(user=request.user)
        return render(request, 'user/profile_user.html', {'myuser': myuser})

    except User.DoesNotExist:
        redirect("/")


'''@login_required(login_url='/user/login/')
def edit_profile(request):
    username = request.user.username
    user = User.objects.get(username=username)
    initialvalues = {'username': username, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return HttpResponseRedirect("user/regOK.html")
            # return render(request, "user/regOK.html", {'message': 'in post.', 'redirect': 'user/view_profile'})
        else:
            return HttpResponseRedirect("user/regOK1.html")
    else:
        form = EditProfileForm(initial=initialvalues)
    return render(request, 'user/profile_edit.html', {'message': 'in get', 'form': form})
'''


@login_required()
def edit_profile(request):
    user = request.user
    form = EditProfileForm(request.POST or None, initial={'first_name': user.first_name, 'last_name': user.last_name,
                                                          'email': user.email})
    if request.method == 'POST':
        # form = EditProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            return HttpResponseRedirect('viewProfile')
            # return render(request, "thanks.html", {'message': 'تغییرات با موفقیت ذخیره شد.', 'redir': '/simorgh/profile/'})
        # else:
        #     print("valid nist")
        #     return HttpResponseRedirect()
    # else:
    #     form = EditProfileForm(initial=init)
    return render(request, 'user/profile_edit.html', {"form": form, "user": user})


@login_required()
def edit_username(request):
    user = request.user
    form = EditUserNameForm(request.POST or None, initial={'username': user.username})
    if request.method == 'POST':
        # form = EditProfileForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.save()
            return HttpResponseRedirect('viewProfile')
            # return render(request, "thanks.html", {'message': 'تغییرات با موفقیت ذخیره شد.', 'redir': '/simorgh/profile/'})
        # else:
        #     print("valid nist")
        #     return HttpResponseRedirect()
    # else:
    #     form = EditProfileForm(initial=init)
    return render(request, 'user/username_edit.html', {"form": form, "user": user})


@login_required()
def edit_password(request):
    user = request.user
    form = EditPasswordForm(request.POST or None, username=user.username)
    if request.method == 'POST':
        # form = EditProfileForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['new_pass'])
            user.save()
            return HttpResponseRedirect('viewProfile')
            # return render(request, "thanks.html", {'message': 'تغییرات با موفقیت ذخیره شد.', 'redir': '/simorgh/profile/'})
        # else:
        #     print("valid nist")
        #     return HttpResponseRedirect()
    # else:
    #     form = EditProfileForm(initial=init)
    return render(request, 'user/username_edit.html', {"form": form, "user": user})


'''def change_password(request):
    user = request.user
    username = request.user.username
    if request.method == 'POST':
        form = ChangePassword(request.POST, username = username)
        if form.is_valid():
            user = Guest.objects.get(username=username)
            user.set_password(form.cleaned_data['new_pass'])
            user.save()
            return render(request, "thanks.html", {'message': 'رمز عبور شما تغییر پیدا کرد.','redir': '/simorgh/home/'} )
    else:
        form = ChangePassword(username=username)
    return render(request, 'Login.html', {'form': form, 'value':"تغییر رمز عبور", 'option': 1})
'''

'''def edit_profile(request):
    user = request.user
    form = EditProfileForm(request.POST or None, initial={'first_name':user.first_name, 'last_name':user.last_name})
    if request.method == 'POST':
        if form.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            return HttpResponseRedirect('%s'%(reverse('profile')))
    context = {
        "form": form
    }
    return render(request, "user/profile_edit.html", context)
'''

'''def forgotpass(request, username=""):
    s = str(request.path).split('/')
    try:
        user = User.objects.get(username=s[-1])
        send_new_password(user)
        return render(request, "thanks.html", { 'message':'گدرواژه جدید به پست الکترونیکی شما فرستاده شد.', 'redir': '/simorgh/login'})
    except User.DoesNotExist:
        return render(request, "thanks.html", {'message':'لینک شما معتبر نمی باشد. لطفا دوباره سعی کنید.', 'redir': '/simorgh/login'})
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
