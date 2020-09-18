from django.shortcuts import render
from .models import chalet


def home(request):
    chalets = chalet.objects.all()
    return render(request, 'home.html', {'chalets': chalets})


def contactUs(request):
    return render(request, 'contactUs.html', {'title': 'contactUs'})


def bookNow(request):
    chalets = chalet.objects.all()
    return render(request, 'book.html', {'chalets': chalets})
