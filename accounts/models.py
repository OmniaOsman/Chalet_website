from django.db import models


class login(models.Model):
    username = models.CharField(max_length=20)
    password = models.IntegerField(default=8)



