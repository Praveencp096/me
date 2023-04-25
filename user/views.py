from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response 
from rest_framework.status import HTTP_200_OK 
from rest_framework import status
from rest_framework.authentication import TokenAuthentication 
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.contrib.auth import authenticate
from .serializers import *

from try_once.utils import get_error

from user.models import UserProfile
from user.serializers import UserProfileSerializer,UserProfileShowSerializer
import random  
import string

def random_string():  
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(5)))  
    str1 += ''.join((random.choice(string.digits) for x in range(5)))  
  
    sam_list = list(str1) # it converts the string to list.  
    random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
    final_string = ''.join(sam_list)  
    return final_string  


class LoginAPI(APIView):  

	permission_classes        = (AllowAny,)
	authentication_classes    = ()
	
	def post(self,request): 

		response_dict = {'success':False}  
		
		get_username  = request.data.get('username')
		get_password  = request.data.get('password')
          
		user = authenticate(username=get_username,password=get_password)
		
		if user:
			t, c= Token.objects.get_or_create(user=user)
			response_dict['token']               = t.key
			response_dict['user_id']             = user.user_id
			response_dict['name']                = user.name
			response_dict['email']                = user.email


			response_dict['success']             = True
			response_dict['message']             = 'Login Succesfull'
			response_dict['status']              = 'success'
		else:
			response_dict['message']     = 'Invalid Credentials'
			response_dict['status']      = 'error'
        
		return Response(response_dict, HTTP_200_OK)


class UserRegister(APIView):

	permission_classes        = (AllowAny,)
	authentication_classes    = ()
	

	def get(self,request):
		response_dict = {}
		response_dict['success'] = False

		users                  = UserProfile.objects.filter(is_active=True)

		response_dict['users'] = UserProfileShowSerializer(
		    instance=users, many=True).data

		response_dict['success'] = True
		response_dict['status']  = 'success'
		response_dict['message'] = 'Users List'

		return Response(response_dict, HTTP_200_OK)

	def post(self,request):
		response_dict = {}
		response_dict['success']     = False

		if UserProfile.objects.filter(username=request.data.get('username')).exists():
			response_dict['status']      = 'error'
			response_dict['message']='Unsername not available'

		else:
			user_register_serializer = UserProfileSerializer(data=request.data)
			if user_register_serializer.is_valid():
				users                 = user_register_serializer.save()
				users.user_id 		  = random_string()
				random_string
				users.set_password(request.data.get('password'))
				users.save()
				token                     = Token.objects.get_or_create(user=users)[0].key
				response_dict['success']   = True
				response_dict['status']    = 'success'
				response_dict['message']   = 'Registered Succesfully'

			else:
				response_dict['status']      = 'error'
				response_dict['message']     = get_error(user_register_serializer)

		return Response(response_dict, HTTP_200_OK)


class LogOut(APIView):
	permission_classes        = (IsAuthenticated,)
	authentication_classes    = (TokenAuthentication,)
	
	def get(self,request):
		response_dict = {}
		
		request.user.auth_token.delete()
		auth.logout(request)

		response_dict['success']   = True
		response_dict['status']    = 'success'
		response_dict['message']   = 'Logout Succesfully'

		return Response(response_dict,HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
	
	serializer_class   = ChangePasswordSerializer
	model              = User
	permission_classes = (IsAuthenticated,)
	
	def get_object(self, queryset=None):	
		obj = self.request.user
		return obj
		
	def update(self, request, *args, **kwargs):
		self.object = self.get_object()
		serializer = self.get_serializer(data=request.data)
		
		if serializer.is_valid():
            # Check old password
			if not self.object.check_password(serializer.data.get("old_password")):
				return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
			self.object.set_password(serializer.data.get("new_password"))
			self.object.save()
			response = {
                'status': 'status',
                'code': status.HTTP_200_OK,
                'message': 'Password updated succesfully',
            }
			
			return Response(response)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)