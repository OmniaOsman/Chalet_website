from django.shortcuts import render


def register(request):
    return render(request, 'signup.html', {'name': 'register'})


def login(request):
    return render(request, 'login.html', {'title': 'login'})


