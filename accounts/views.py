
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import *


def register(request):
    if request.method=="POST":
        username=request.POST['username']
        name=request.POST['name']
        mobile= request.POST['mob']
        email = request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if reg.objects.filter(username=username).exists():
                messages.info(request,"User name is alredy exist!!")
                return redirect('register')
            elif reg.objects.filter(email=email).exists():
                messages.info(request,"Email is alredy exist!!")
                return redirect('register')
            else:
                user=reg.objects.create(username=username,name=name,mobile=mobile,email=email,password=password1)
                user.save()
                messages.info(request,"Registration completed successfully")
                return redirect('register')

        else:
            messages.info(request, "Password did't match!!")
            return redirect('register')
    else:
        return render(request,'register.html')



def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid User!!")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')