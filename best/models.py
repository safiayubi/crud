from django.db import models
from django.forms import CharField, PasswordInput

# Create your models here.
class User(models.Model):
    id =models.IntegerField(primary_key= True)
    name =models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)