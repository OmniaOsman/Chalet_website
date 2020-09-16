from django.db import models


class chalets(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    price = models.IntegerField(default=5)
    status = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return chalets.city
