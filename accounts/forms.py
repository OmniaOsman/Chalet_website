from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm): 
    email     = forms.EmailField(widget=forms.EmailInput(
        attrs={'class'      : 'form-control', 
               'type'       : "text",
               'class'      : "form-control",
               'placeholder': "Email"}))
    password1 = forms.CharField(min_length=8, label='Password', widget=forms.PasswordInput(
        attrs={'id'         : "password-field",
               'class'      : 'form-control', 
               'type'       : "password",
               'class'      : "form-control",
               'placeholder': "Password",
               'toggle'     : "#password-field",}))
    password2 = forms.CharField(min_length=8, label='Confirm Password', 
                               widget=forms.PasswordInput(
        attrs={'id'         :"password-field",
               'class'      : 'form-control', 
               'type'       : "password",
               'class'      : "form-control",
               'placeholder': "Confirm Password",}))
    class Meta:
        model  = User
        fields = ('email', 'password1', 'password2')


class LoginForm(forms.Form):
    email     = forms.CharField(widget=forms.EmailInput(
        attrs={'class'      : 'form-control', 
               'type'       : "text",
               'class'      : "form-control",
               'placeholder': "Email"}))
    password  = forms.CharField(min_length=8, label='Password', widget=forms.PasswordInput(
        attrs={'id'         : "password-field",
               'class'      : 'form-control', 
               'type'       : "password",
               'class'      : "form-control",
               'placeholder': "Password",
               'toggle'     : "#password-field",}))
    class Meta:
        model = User
        fields = ('email', 'password',)
