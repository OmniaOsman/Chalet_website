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
