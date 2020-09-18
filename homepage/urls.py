from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('book/', views.bookNow, name='book'),
]
