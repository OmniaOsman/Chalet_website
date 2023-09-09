from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.contactUs, name='contact'),
    # path('book/', views.bookNow, name='book'),
    path('accomodation', views.accomodation, name='accomodation'),
    path('<slug:slug>/', views.ChaletDetails.as_view(), name='chalet_details'),
    path("contact/success/", views.successView, name="success"),
    path("aboutus", views.aboutus, name="aboutus"),
] 
