"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from Project import settings
from . import views

app_name = 'restaurant'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , views.index , name = 'index'),
    url(r'^branch/(?P<branch_id>[0-9]+)/$', views.show_branch_menu, name='branch menu'),
    url(r'^branch', views.branch, name='branch'),
    url(r'^menu/(?P<food_name>.+)/', views.food, name='food'),  # TODO: fix the url some way!
    url(r'^menu', views.menu, name = 'menu'),
    url(r'^order', views.order, name = 'order'),
    url(r'^search', views.search, name='search'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)