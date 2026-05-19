from django.db import models
from django.core.validators import FileExtensionValidator

class Printing(models.Model):
    name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=12)
    desc = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=500)
    body = models.TextField()
    printing = models.ForeignKey(Printing, on_delete=models.SET_DEFAULT, default='Uzbekistan')
    genre = models.ForeignKey(Genre, on_delete=models.SET_DEFAULT, default='General')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title