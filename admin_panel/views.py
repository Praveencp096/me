from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
#from .forms import UserRegistrationForm, UserLoginForm
from .models import*



def ulogin(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            password=request.POST.get('pwd')
            login=user.objects.get(email=email,pwd=password)
            request.session['name']=login.name
            request.session['id']=login.id
            return redirect('uindex')
        except user.DoesNotExist as e:
            messages.info(request,'Incorrect Password or Email')
    return render(request,'user/ulogin.html')

def ureg(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        pwd=request.POST.get("pwd")
        pwd2=request.POST.get("cpwd")
        

        if pwd==pwd2:
            if user.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
        
            elif user.objects.filter(phone=phone).exists():
                messages.info(request,'Phone Number  already exists')
            else:
                savevalue=user(name=name,email= email, 
                            phone=phone,pwd=pwd)
                savevalue.save()
                return redirect("ulogin")
        else:
             messages.info(request,'password not match')
    return render(request,'user/ureg.html')



def adminlogin(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            password=request.POST.get('pwd')
            login=admins.objects.get(email=email,pwd=password)
            request.session['name']=login.name
            request.session['id']=login.id
            return redirect('uindex')
        except admins.DoesNotExist as e:
            messages.info(request,'Incorrect Password or Email')
    return render(request,'admin/alogin.html')

def ureg(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        pwd=request.POST.get("pwd")
        pwd2=request.POST.get("cpwd")
        

        if pwd==pwd2:
            if admins.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
        
            elif admins.objects.filter(phone=phone).exists():
                messages.info(request,'Phone Number  already exists')
            else:
                savevalue=admins(name=name,email= email, 
                            phone=phone,pwd=pwd)
                savevalue.save()
                return redirect("alogin")
        else:
             messages.info(request,'password not match')
    return render(request,'admin/areg.html')