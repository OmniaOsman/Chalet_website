from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from homepage.models import Chalet, Contact
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.views import View
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView



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
    return render(request, "contact.html", {"form": form})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")

# def bookNow(request):
#     chalets = Booking.objects.all()
#     return render(request, 'book.html', {'chalets': chalets})



def aboutus(request):
    return render(request, 'about.html')


def accomodation(request):
    return render(request, 'accomodation.html')


class ChaletDetails(DetailView):
    model = Chalet
    slug_field = 'slug'
    template_name = 'chalet-details.html'
    context_object_name = 'chalet'


class HomeView(View):
    def get(self, request):
        chalets = Chalet.objects.all()
        
        paginator = Paginator(chalets, 3)  # Show 25 contacts per page.
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        context = {
            'chalets': page_obj,
        }
        return render(request, 'home (2).html', context)
    