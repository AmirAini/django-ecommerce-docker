from django.urls import path

from . import views


# refer to this urls
app_name = 'store'


urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]
