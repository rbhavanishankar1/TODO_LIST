from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import  settings
from django.core.mail import send_mail
import random
from uuid import uuid4

# Create your views here.

def register_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        email=request.POST.get('email')
        
        if User.objects.filter(username = username).exists():
            messages.error(request,'Username Aready Exits',extra_tags='danger')
            return redirect('/register/')
        
        elif User.objects.filter(email = email).exists():
            messages.error(request,'Email ID Already Exits Please Enter Valid email ID',extra_tags='danger')
            return redirect('/register/')
        
        elif (password !=  confirm_password):
            messages.error(request,'Password and Confirm_password are not same',extra_tags='danger')
            return redirect('/register/')
        
        elif register_model.objects.filter(phone = phone).exists():
            messages.error(request,'Phone number Already Exists')
            return redirect('/register/')

        else:
            user=User.objects.create(username=username,
                                          first_name=first_name,
                                          last_name=last_name,
                                          email=email
                                          )
            register_model.objects.create(phone=phone,
                                          gender=gender).save()
            user.set_password(password)
            user.save()
            messages.info(request,'Registration Sucess')
            return redirect('/login/')
    return render(request=request,template_name='register.html',context={'Register':'register'})





def login_view(requset):
    if requset.method == 'POST':
        username=requset.POST.get('username')
        password=requset.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(requset,'INVALID USERNAME',extra_tags='danger')
            return redirect('/login/')
        
        user=authenticate(username = username,password=password)

        if user is None:
            messages.info(requset,'INVALID PASSWORD',extra_tags='danger')
            return redirect('/login/')

        else:
            login(requset,user)
            return redirect('/home/')
    res1=User.objects.all()
    return render(request=requset,template_name='login.html',context={'res1':res1})

def logout_view(request):
    logout(request)
    return redirect('/login/')


generated_otp=None
username1=None
generated_token=None
user=None
def user_verify_view(request):
    if request.method=='POST':
        global username1
        username1=request.POST.get('username')

        if User.objects.filter(username=username1).exists():
            global generated_otp
            generated_otp=random.randint(1000,9999)
            global user
            user=User.objects.get(username=username1).email
            
            send_mail(
                subject="DON'T REPLY IT IS COMPUTER GENERATED MESSAGE",
                message=f'your required otp for reset password  is  :{generated_otp}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user]

            )
            global generated_token
            generated_token=uuid4()


            return redirect(f'/otp/{generated_token}')
        else:
            messages.info(request, "USER DOESN'T EXITS",extra_tags="danger")
            return redirect('/user_verify')
    return render(request=request,template_name='user_verify.html')

def otp_view(request,token):
    if token==str(generated_token):
        if request.method=='POST':
            otp=request.POST.get('OTP')
            if int(otp)==int(generated_otp):
                return redirect(f'/change_password/{generated_token}')
            else:
                messages.info(request,"INVALID OTP",extra_tags="danger")
                return HttpResponseRedirect(request.path_info)
    return render(request=request,template_name='otp.html')


def change_password_view(request,token):
    if token==str(generated_token):
        if request.method=='POST':
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')
            if password == confirm_password:
                user =User.objects.get(username=username1)
                user.password=password
                user.set_password(password)
                user.save()
                return redirect('/login/')
            else:
                messages.info(request,'PASSWORD AND CONFIRM PASSWORD ARE NOT SAME')
                return HttpResponseRedirect(request.path_info)
    return render(request=request,template_name='change_password.html')

