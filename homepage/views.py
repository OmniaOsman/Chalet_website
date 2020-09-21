from django.contrib import messages
from django.shortcuts import render, redirect
from .models import chalet, contact, bookNow


def home(request):
    chalets = chalet.objects.all()
    return render(request, 'home.html', {'chalets': chalets})


def contactUs(request):
    """ form = contactForm()
    if request.method == 'POST':
        form.save()
        # send email code goes here
        return HttpResponse('Thanks for contacting us!')
    else:
        form = contactForm()"""
    return render(request, 'contactUs.html', {'form': 'form'})


def bookNow(request):
    chalets = chalet.objects.all()
    return render(request, 'book.html', {'chalets': chalets})
