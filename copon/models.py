from django.db import models
from django.db import connections
from django.contrib.auth.models import User 
import uuid







#Create your models here.

SUBSCRIPTION=(
   ('M','MONTHLY'),
   ('Y','YEARLY'),
)

class copons(models.Model):
     cname =models.CharField(max_length=10, blank=True)
     cnumber =models.CharField(max_length=14)
    
    
     class Meta:
        db_table = "phonenumberlist"

class profile(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   pro=models.BooleanField(default=False)
  
   subscriptiontype=models.CharField(max_length=100,choices=SUBSCRIPTION,)

class Payment_details(models.Model):
    customer_name= models.CharField(max_length=28, blank=True)
    customer_email =models.CharField(max_length=23, blank=True)
    payment_id =models.CharField(max_length=49, blank=True)
    
   

    class Meta:
        db_table = "payment_info"
class Payment_details_customer(models.Model):


    
    cardname= models.CharField(max_length=20, blank=True)
    phonenumber =models.CharField(max_length=23, blank=True)
    email =models.CharField(max_length=20, blank=True)
    address =models.CharField(max_length=40, blank=True)
    city =models.CharField(max_length=20, blank=True)
    country =models.CharField(max_length=20, blank=True)
    state =models.CharField(max_length=20, blank=True)
    postcode =models.CharField(max_length=20, blank=True)
    paymentstatus=models.CharField(max_length=20, blank=True)
    paymentid=models.CharField(max_length=20, blank=True)
   
   

    class Meta:
        db_table = "Payment_details_customer"     

class Subscription_details(models.Model):
   sname= models.CharField(max_length=20, blank=True)
   email =models.CharField(max_length=20 )
   customer_id=models.CharField(max_length=20 )
   session_id=models.CharField(max_length=40, blank=True)
   subscription_status=models.CharField(max_length=40, blank=True)
   class Meta:
        db_table = "Subscription_details"   
