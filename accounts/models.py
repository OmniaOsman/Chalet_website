from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, Group, Permission, UserManager    


class CustomUserManager(UserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    
    def _create_user(self, email, password, **extra_fields):
            email = self.normalize_email(email)
            user  = self.model(email=email, **extra_fields)
            user.password = make_password(password)
            user.save(using=self._db)
            return user
        
    def create_user(self, email, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
            return self._create_user(email, password, **extra_fields)
        
        

class User(AbstractUser):
    email    = models.EmailField(max_length=254, unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    objects = CustomUserManager() # use the custom manager
    
    def __str__(self):
        return self.email
