from django.db import models
# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100,default='')
    emp_code = models.CharField(max_length=5,default='')
    mobile = models.CharField(max_length=15,default='')
    Email =models.EmailField(max_length=300,default='')
    Password =models.CharField(max_length=15,default='')
    Address =models.CharField(max_length=300,default='')
