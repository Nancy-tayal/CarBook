from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth.models import auth
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def login(request):
    if request.method == 'POST' :
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None :        
            auth.login(request, user)
            return redirect('/')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Invalid Password!")
                return redirect('login')

            else:
                messages.info(request, "Invalid Email!")
                return redirect('login')

    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exist!')
            return redirect('register')
        elif password1 != password2:
            messages.info(request, "Password and Confirm Password doesn't match!")
            return redirect('register')
        else:
            user = User.objects.create_user(name=name, email=email, phone=phone, password=password1)
            user.save()
            subject = 'Registration Confirmation'
            message = f'Hi {user.name}, thank you for registering in CarRental.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list,fail_silently=False )
            return redirect('home')
        
    else:
        return render(request, 'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')