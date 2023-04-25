from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin

from user.models import UserProfile
# Register your models here.

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ("username",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        exclude=[]

class CustomUserAdmin(UserAdmin):
 
    fieldsets = (
        (None, {'fields': ('username', 'password','email')}),
        (('Personal info'), {'fields': ('user_id','name','mobile', 'address','pincode')}),

        (('Permissions'), {'fields': ('is_active', 'is_staff','is_superuser',
                                       'groups', 'user_permissions')}),
        (('dates'), {'fields': ('last_login',  )}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2',)}
        ),
    )

    form      = CustomUserChangeForm 
    add_form  = CustomUserCreationForm

admin.site.register(UserProfile,CustomUserAdmin)