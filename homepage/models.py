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
        return self.name
    


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email     = models.EmailField(max_length=254)
    massage   = models.TextField()
    
    def __str__(self):
        return self.name


class BookNow(models.Model):
    chalet_name      = models.ForeignKey("Chalet", on_delete=models.CASCADE)
    No_of_persons    = models.IntegerField(default=2)
    reservation_date = models.DateField(auto_now=False, auto_now_add=False)
    No_of_days       = models.IntegerField()
    
    def __str__(self):
        return self.chalet_name
