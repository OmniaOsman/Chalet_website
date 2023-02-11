from django.contrib import messages
from django.shortcuts import render, redirect
from homepage.models import Chalet, Contact, BookNow


def home(request):
    chalets = Chalet.objects.all()
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
    chalets = BookNow.objects.all()
    return render(request, 'book.html', {'chalets': chalets})
