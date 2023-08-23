import random
import string

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Token

random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=28))

def HomePage(request):
    return render(request, 'home.html')

def RigisterPage(request):
    if request.method=='POST':
        username =request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if not username or not email :
            return HttpResponse("Username and email are required")
        elif pass1 != pass2:
            return HttpResponse("password not match")
        else:
            my_user = User.objects.create_user(username,email,pass1)
            this_token = random_str
            token = Token.objects.create(user=my_user, token=this_token)
            my_user,token.save()

    return render(request, 'register.html')

def LoginPage(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username,password=pass1)

        if user is not None:
            login(request,user)
            return HttpResponse('welcome ')
        else:
            return HttpResponse('User name or password incorrent')

    return render(request, 'login.html')