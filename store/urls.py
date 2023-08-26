from django.contrib import admin
from django.urls import path, include
from . import views

#refer to this urls
app_name = 'store'

urlpatterns = [ 
    path('',views.all_products,name='all_products')
]