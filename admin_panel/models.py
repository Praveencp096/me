from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from user.models import UserProfile


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models






from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=500)
    pwd=models.CharField(max_length=10)
    def _str_(self) :
        return self.name 
    
class admins(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=500)
    pwd=models.CharField(max_length=10)
    name=models.ForeignKey(user,on_delete=models.CASCADE)
    def _str_(self) :
        return self.name 
    
