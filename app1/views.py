from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def signup_in(request):
    if request.method == "POST":
        if "register" in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
        

            myuser = User.objects.create_user(username, email, pass1)
            myuser.save()

            messages.success(request, "Successfully!")
            return redirect('signup_in')     
          
        elif "login" in request.POST:
            usernamel = request.POST['usernamel']
            passl = request.POST['passl']

            user = authenticate(username = usernamel, password = passl)

            if user is not None:
                login(request, user)
                if request.user.is_authenticated:
                    user_not_login = "hidden"
                    user_login = "show"
                else:
                    user_not_login = "show"
                    user_login = "hidden"
                context = {'user_login': user_login, 'user_not_login': user_not_login}
                return render(request, "app/homepage.html", context)

            else: 
                messages.error(request, "Wrong!")
                return redirect('signup_in')
    return render(request, "app/login.html")


def signout(request):
    logout(request)
    return redirect('signup_in')

    
# def signup(request):
#     if request.method == "POST":
#         usernamel = request.POST['usernamel']
#         passl = request.POST['passl']

#         user = authenticate(username = usernamel, password = passl)

#         if user is not None:
#             login(request, user)
#             return render(request, "app/homepage.html")

#         else: 
#             messages.error(request, "Wrong!")
#             return render(request, 'app/login.html')
            
            

def home(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_login': user_login, 'user_not_login': user_not_login}
    return render(request, 'app/homepage.html', context)

def find(request):
    tutors = TUTOR.objects.all()
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'tutors': tutors, 'user_login': user_login, 'user_not_login': user_not_login}
    return render(request, 'app/Timkiem.html', context)

def tutor(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_login': user_login, 'user_not_login': user_not_login}
    return render(request, 'app/tutor.html', context)
#information of a tutor when you click on profile button
def info(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_login': user_login, 'user_not_login': user_not_login}
    return render(request, 'app/tutor_profile.html', context)

def reset_pass(request):
    return render(request, 'app/reset_password.html')

