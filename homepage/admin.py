from django.contrib import admin
from .models import chalets


@admin.register(chalets)
class chaletAdmin(admin.ModelAdmin):
    list_display = ('city', 'image')
