from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def HomePage(request):
    return render(request, 'home.html')

def RigisterPage(request):
    if request.method=='POST':
        username =request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("password not match")
        else:
            my_user = User.objects.create_user(username,email,pass1)
            my_user.save()
            print(username,email,pass1)

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