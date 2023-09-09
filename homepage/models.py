from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from accounts.models import User
from datetime import datetime


class Chalet(models.Model):
    name        = models.CharField(max_length=150)
    city        = models.CharField(max_length=50)
    price       = models.DecimalField(max_digits=8, 
                                      decimal_places=2)
    No_of_rooms = models.IntegerField(default=2)
    slug        = models.CharField(max_length=150, 
                                   blank=True)
    available   = models.BooleanField(default=True)
    description = models.TextField()
    image       = models.ImageField(upload_to='chalets')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("home:chalet_detail", 
                       kwargs = {
                           "slug": self.slug,
                        })
    
    

    

class Contact(models.Model):
    name      = models.CharField(max_length=50)
    email     = models.EmailField(max_length=254)
    massage   = models.TextField()
    
    def __str__(self):
        return self.name



