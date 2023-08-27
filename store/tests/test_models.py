from django.test import TestCase
from store.models import Category, Product, User


class TestCategoryModel(TestCase):
    
    # setup test class
    def setUp(self):
        self.data = Category.objects.create(name='bed',slug='bed')
    
    def test_user_can_create_cateogry(self):
        data = self.data
        self.assertTrue(isinstance(data,Category))
        
    def test_category_model_return_name(self):
        data = self.data
        self.assertEqual('bed',str(data))
        
class TestProductModel(TestCase):
    
    def setUp(self):
        category = Category.objects.create(name='bed',slug='bed')
        user = User.objects.create(username='admin')
        self.data = Product.objects.create(
            category = category,
            created_by = user,
            title = 'futon',
            slug = 'futon',
            description = 'soft and wide',
            price = 99.99,
            is_active = True,
            image='image'
        )
    
    def test_user_can_create_product(self):
        product = self.data
        self.assertTrue(isinstance(product,Product))
        self.assertEqual('futon',str(product))