from os import name

from django.shortcuts import render
from .models import chalets


def home(request):
    chalet_name = [chalets.objects.all()]
    return render(request, 'home.html', {'chalet_name': chalet_name})


def contactUs(request):
    return render(request, 'contactUs.html', {'title': 'contactUs'})


