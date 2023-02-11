from django.db import models


class Chalet(models.Model):
    name        = models.CharField(max_length=150)
    city        = models.CharField(max_length=50)
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    No_of_rooms = models.IntegerField(default=2)
    available   = models.BooleanField(default=True)
    description = models.TextField()
    image       = models.ImageField()

    def __str__(self):
        return Chalet.name


class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname  = models.CharField(max_length=50)
    email     = models.EmailField(max_length=254)
    phone     = models.CharField(max_length=14)
    massage   = models.TextField()
    
    def __str__(self):
        return Contact.firstname


class BookNow(models.Model):
    chalet_name      = models.ForeignKey("Chalet", on_delete=models.CASCADE)
    No_of_persons    = models.IntegerField(default=2)
    reservation_date = models.DateField(auto_now=False, auto_now_add=False)
    No_of_days       = models.IntegerField()
    
    def __str__(self):
        return BookNow.chalet_name
