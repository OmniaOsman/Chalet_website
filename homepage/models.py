from django.db import models


class chalet(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    price = models.IntegerField(default=5)
    status = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='static')

    def __str__(self):
        return chalet.city


class contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    massage = models.TextField()


class bookNow(models.Model):
    chalet_name = models.CharField(max_length=150)
    number_of_room = models.IntegerField(default=2)
    number_of_person = models.IntegerField(default=2)
    number_of_children = models.IntegerField(default=2)

    


