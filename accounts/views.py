from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.save()
            auth_login(request, username)
            return redirect('home')
    return render(request, 'signup.html', {'form': form})


def login(request):
    return render(request, 'login.html', {'title': 'login'})


