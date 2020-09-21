from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib.auth import login as auth_login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']
        if psw == psw_repeat:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=psw, email=email)
                user.save()
                print("User created!")
            return redirect('/')
        else:
            messages.info(request, 'password not matching !')
            return redirect('register')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html', {'title': 'login'})


def logout(request):
    auth.logout(request)
    return redirect('/')
