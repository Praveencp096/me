from rest_framework import serializers
from django.contrib.auth.models import User,auth
from rest_framework import exceptions
from django.contrib.auth import authenticate

from .models import *

