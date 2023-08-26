from unicodedata import category
from django.shortcuts import get_object_or_404, render, get_list_or_404
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

def show_product(request,product_id):
    product = Product.objects.get(id=product_id)
    return render(request,'store/product.html',{'product':product})

def category_list(request, category_slug):
    products = Product.objects.filter(category__slug=category_slug).prefetch_related('category')
    return render(request,'store/category.html',{'products':products,'category':category_slug})