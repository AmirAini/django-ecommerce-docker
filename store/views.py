from django.shortcuts import render
from .models import Product,Category


# get the categories for home
def all_categories(request):
    categories = Category.objects.all()
    
    return {
        'categories':categories
    }

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request,'store/home.html',{'products':products})