from rest_framework import serializers
from django.contrib.auth.models import User,auth
from rest_framework import exceptions
from django.contrib.auth import authenticate

from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model  = UserProfile
		fields = ('username','password','user_id','name','email', 'mobile', 'pincode', 'address')

class UserProfileShowSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserProfile
        fields = ('id','user_id','name','email')

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)