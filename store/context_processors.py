from .models import Category

# get the categories for home
def all_categories(request):
    categories = Category.objects.all()
    
    return {
        'categories':categories
    }
