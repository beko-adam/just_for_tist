import email
from sre_constants import CATEGORY_DIGIT
from telnetlib import STATUS
from unicodedata import category, name
from django.db import models

# Create your models here.

class Customer(models.Model):


    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    data_create = models.DateField(auto_now_add=True, null=True)


    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)


#Tage table
class Tag(models.Model):
    

    name = models.CharField(max_length=100, null=True)
   

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)


class Product(models.Model):

    CATEGORY = (


        ('indoor', 'indoor'),
        ('out door', 'out door'),
    )

    name = models.CharField( max_length=100, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.CharField(max_length=100, null=True)
    data_created = models.DateField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)




class Order(models.Model):

    STATUS = (   
        ('pending', 'pending'),
        ('out for delivery', 'out for deliver'),
        ('Delivered', 'delivered'),
        )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    data_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)



    