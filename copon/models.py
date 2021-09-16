from django.db import models
from django.db import connections




#Create your models here.

class copons(models.Model):
     cname =models.CharField(max_length=10, blank=True)
     cnumber =models.CharField(max_length=14)
    
    
     class Meta:
        db_table = "phonenumberlist"


