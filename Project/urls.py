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
    url(r'^search/', views.search),
    url(r'^restaurant/', include('restaurant.urls')),
    # url(r'^$', views.index,name = 'index')
    url(r'^employee/authentication/check',viewsForEmployee.authentication_check),
    url(r'^clerk/authentication/check',viewsForEmployee.authentication_check),
    url(r'^employee/', viewsForEmployee.hello),
    url(r'^cook/dutyList', viewsForEmployee.duty_list_cook),
    url(r'^cook/setRecipe', viewsForEmployee.set_recipe),
    url(r'^cook/addAbility', viewsForEmployee.add_ability),
    url(r'^cook/setOffer', viewsForEmployee.set_food_offer),
    url(r'^warehouseman/addMaterial', viewsForEmployee.add_material),
    url(r'^warehouseman/getReport', viewsForEmployee.get_warehouse_report),
    url(r'^clerk/ordering' , viewsForEmployee.get_order),
    url(r'^waiter/dutyList' , viewsForEmployee.duty_list_waiter),
    url(r'^deliveryman/dutyList', viewsForEmployee.duty_list_deliveryman),
    url(r'^parkingman/', viewsForEmployee.authentication_check),
    url(r'^clerk/authentication', viewsForEmployee.clerk_authentication),
    url(r'^deliveryman/authentication', viewsForEmployee.delivery_authentication),
    url(r'^waiter/authentication', viewsForEmployee.waiter_authentication),
    url(r'^user/', include('user.urls')),

    # url(r'^thanks/', views.thanks),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)