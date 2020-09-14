from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'title': 'home'})


def contactUs(request):
    return render(request, 'contactUs.html', {'title': 'contactUs'})


