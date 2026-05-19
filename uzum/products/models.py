from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)

class Product(models.Model):
    COLORS = (
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('red', 'Red')
    )
    
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='General')
    summary = models.CharField(max_length=400, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(max_length=10)
    color = models.CharField(max_length=20, choices=COLORS, null=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)