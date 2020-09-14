from django.db import models


class chalets(models.Model):
    city = models.CharField(max_length=25)
    image = models.ImageField(upload_to='chalets-img')
    content = models.TextField(default=' ')

    def __str__(self):
        return chalets.city
