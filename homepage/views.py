from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from homepage.models import Chalet, Contact, BookNow
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
    chalets = Chalet.objects.all()
    return render(request, 'home.html', {'chalets': chalets})


def contactUs(request):
    # """ form = contactForm()
    # if request.method == 'POST':
    #     form.save()
    #     # send email code goes here
    #     return HttpResponse('Thanks for contacting us!')
    # else:
    #     form = contactForm()"""
    # return render(request, 'contactUs.html', {'form': 'form'})
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "contactUs.html", {"form": form})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")

def bookNow(request):
    chalets = BookNow.objects.all()
    return render(request, 'book.html', {'chalets': chalets})
