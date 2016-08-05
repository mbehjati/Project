# from django.conf.urls import url
# from user import views
#
# urlpatterns = [
#     url(r'^register$', views.register, name='register'),
#     url(r'^login$', views.login, name='login'),
#     url(r'^logout$', views.logout, name='logout'),
#     # url(r'^viewProfile$', views.view_profile, name='viewProfile'),
#     # url(r'^CommentFood$', views.foodcommenting, name='commentForFood'),
# ]
from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^profile', views.view_profile, name='viewProfile'),
    url(r'^editProfile$', views.edit_profile, name='EditProfile'),
    url(r'^editUserName$', views.edit_username, name='EditUserName'),
    url(r'^editPassword$', views.edit_password, name='EditPassword'),
    url(r'^reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        views.reset_confirm, name='reset_confirm'),
    url(r'^reset/$', views.reset, name='reset'),
    url(r'^orders/(?P<order_id>[0-9]+)/comment', views.comment, name='comment'),
    url(r'^orders/(?P<order_id>[0-9]+)', views.order_detail, name='detail'),
    url(r'^orders', views.costumer, name='costumer'),
    # url(r'^forgotPass$', views.forgotpass(), name='forgotpassword'),
    # url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset',
    #     {'post_reset_redirect': '/accounts/password/reset/done/'}),
    # url(r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    # url(r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
    #     'django.contrib.auth.views.password_reset_confirm',
    #     {'post_reset_redirect': '/accounts/password/done/'}),
    # url(r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
    # url(r'^CommentFood$', views.foodcommenting, name='commentForFood'),
]
