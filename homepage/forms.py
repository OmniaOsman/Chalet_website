""" from .models import contact

from django import forms


class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['firstname', 'lastname', 'email', 'phone', 'massage'] """
