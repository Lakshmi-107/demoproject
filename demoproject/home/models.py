from django.db import models


# Create your models here.
#category table:id, name, desc,image,date
#product table:id, name, image, category_id,price,avalaible,date,stock

class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category/images/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product/images/')
    available = models.BooleanField(default=False)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
