from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser): 
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], null=True, blank=True)
    notification_preference = models.CharField(max_length=20, choices=[('E', 'Email'), ('S', 'SMS'), ('N', 'None')], default='E')
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    

    def __str__(self):
        return self.username
