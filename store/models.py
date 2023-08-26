from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=225, unique=True) # slugfield param 
    
    #declare meta data
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product')
    created_by = models.ForeignKey(User ,on_delete=models.CASCADE,related_name="owner")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField()
    price = models.DecimalField(max_digits=4,decimal_places=2)    
    is_active = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural= 'products'
        ordering = ['-created_at'] #order by latest created at
        
    def __str__(self)->str:
        return self.title