from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    package = models.IntegerField(default=0)
    extra = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    totalAmount = models.DecimalField(decimal_places=2,max_digits=20)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    status = models.CharField(choices=[
        ('Placed','Placed'),
        ('Packed','Packed'),
        ('Delivered','Delivered'),

    ],max_length=100)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(max_length=100)

    def __str__(self):
        return self.order_id

class CustomerDetails(models.Model):
    class Meta:
        verbose_name_plural = 'Customer Details'

    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    address = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Card(models.Model):
    order = models.OneToOneField(Order,on_delete=models.CASCADE)
    number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=10)
    cvc = models.IntegerField()

    def __str__(self):
        return self.number


    

