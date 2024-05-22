from django.db import models
from users.models import CustomUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    made_in = models.CharField(max_length=100)



class Order(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    quantity = models.IntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"Order by {self.username}"