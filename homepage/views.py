from django.shortcuts import render
from .models import chalets


def home(request):
    chalet = chalets.objects.all()
    return render(request, 'home.html', {'chalet': chalet})


def contactUs(request):
    return render(request, 'contactUs.html', {'title': 'contactUs'})


