from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
import uuid

class User(AbstractUser):
    identifier = models.IntegerField(unique=True, null=True, blank=True)
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    ceo_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.username
    
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user = instance)



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")
    username = models.CharField(max_length=30, unique=True) #student name
    identifier = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return str(self.user.identifier)
    

class Company(models.Model):
    user = models.OneToOneField(User,related_name="company",on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True) ##company name
    identifier = models.CharField(max_length=30, unique=True)
    ceo_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='company_images/', null=True, blank=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username