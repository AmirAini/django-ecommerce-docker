from django.shortcuts import render

from .models import Category, Product


# get the categories for home
def all_categories(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }


# Create your views here.
def product_all(request):
    products = Product.product.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/product.html', {'product': product})


def category_list(request, category_slug):
    products = Product.objects.filter(category__slug=category_slug).prefetch_related('category')
    return render(request, 'store/category.html', {'products': products, 'category': category_slug})
