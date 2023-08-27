from urllib import response

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import product_all


class TestViewResponses(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
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
        self.client = Client()
    
    def test_user_can_visit_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        
    def test_user_can_visit_product_detail(self):
        response = self.client.get(reverse("store:product_detail", args=[1]))
        self.assertEqual(response.status_code,200)
    
    def test_user_can_visit_product_detail(self):
        response = self.client.get(reverse("store:category_list", args=['bed']))
        self.assertEqual(response.status_code,200)
    
    def test_homepage_html(self):
        request = HttpRequest()
        
        # calling the view method
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code,200)
        self.assertIn('Home',html)
    
    def test_allowed_hosts(self):
        response = self.client.get('/',HTTP_HOST = 'abc.com')
        self.assertEqual(response.status_code,200)
    
    def test_view_function(self):
        request = self.factory.get('bed')
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code,200)
    