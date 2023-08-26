from unicodedata import category
from django.contrib import admin
from django.urls import path, include
from . import views

#refer to this urls
app_name = 'store'

urlpatterns = [ 
    path('',views.all_products,name='all_products'),
    path('<int:product_id>',views.show_product,name='product_detail'),
    path('<slug:category_slug>',views.category_list,name='category_list'),
]