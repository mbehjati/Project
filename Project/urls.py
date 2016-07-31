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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static

import restaurant
from Project import settings
from restaurant import views
from employee import viewsForEmployee

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/', views.get_name),
    url(r'^restaurant/', include('restaurant.urls')),
    # url(r'^$', views.index,name = 'index')
    url(r'^employee/authentication/check',viewsForEmployee.authentication_check),
    url(r'^employee/', viewsForEmployee.hello),
    # url(r'^thanks/', views.thanks),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)