from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Order(models.Model):

    

    order_id = models.CharField(max_length=200)
    totalProducts = models.IntegerField()
    unitAmount = models.DecimalField(decimal_places=2,max_digits=20)
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
    payment_id = models.CharField(max_length=100)

    def __str__(self):
        return self.order_id

class CustomerDetails(models.Model):
    class Meta:
        verbose_name_plural = 'Order Details'

    order = models.ForeignKey(Order,on_delete=models.CASCADE)
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
    


    



    
