from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        get_confirm_password=request.POST.get('pass2')
        if get_password != get_confirm_password:
            messages.info(request,'Password is not matching')
            return redirect('/auth/signup/')
        
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,"Email is already Taken")
                return redirect ('/auth/signup/')
        except Exception as identifier:
            pass  
        myuser=User.objects.create_user(get_email,get_email,get_password)
        myuser.save()
        # to login the user automaticaly after signup process
        myuser=authenticate(username=get_email,password=get_password)
        
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'User Created & Logged In Successfully')
            return redirect('/')
            
    return render(request,'signup.html')

def handleLogin(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        myuser=authenticate(username=get_email,password=get_password)
        
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'You are Logged In Successfully')
            return redirect('/')
        else:
            messages.error(request,'Username or Password is incorrect')
    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request,'You have been logged out successfully')
    return render(request,'login.html')


# superuser
# name: dipendra@gmail.com
# email: dipendra@gmail.com
# password: super12