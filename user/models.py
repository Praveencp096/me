from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils import timezone
from datetime import datetime

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, password, 
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        now = timezone.now() 
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username,
                          is_active=True, is_staff=is_staff,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True,
                                 **extra_fields)


class UserProfile(AbstractUser):
    user_id         = models.CharField(max_length=10,blank=True,null=True)
    name     		= models.CharField(max_length=50,blank=False,null=False)
    email           = models.CharField(max_length=20,blank=True,null=False)
    mobile          = models.CharField(max_length=20,blank=True,null=True)
    address         = models.CharField(max_length=100,blank=True,null=True)
    pincode         = models.CharField(max_length=10,blank=True,null=True)

    created_by      = models.ForeignKey('self',blank=True,null=True,on_delete=models.SET_NULL)
    is_active       = models.BooleanField(null=False,blank=True,default=True)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    objects=CustomUserManager()

    def __unicode__(self):
    	return str(self.name)

    def __str__(self):
    	return self.name

    