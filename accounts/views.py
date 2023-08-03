from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, views
from django.urls import reverse_lazy
from django.views import generic
from .models import User
from .forms import SignUpForm, LoginForm



class SignUpView(generic.CreateView):
    form_class    = SignUpForm
    template_name = 'signup.html' 
    
    def form_valid(self, form):
        # get data from form
        email     = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        # save user in database with hash password
        user      = User(email=email, password=password1)
        user.set_password(password1)
        user      = user.save()
        # authenticate, login, and redirect to home
        user      = authenticate(email=email, password=password1)
        login(self.request, user)
        return redirect('home')



class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class    =  LoginForm 

    def form_valid(self, form):
        # get data from for and authenticate
        email    = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user     = authenticate(email=email, password=password)
        
        if user is not None:
            login(self.request, user)
            return redirect('home')
        else:
            messages.info(self.request, 'invalid username or password')
            return redirect('login')



class LogoutView(views.LogoutView):
    next_page = '/'