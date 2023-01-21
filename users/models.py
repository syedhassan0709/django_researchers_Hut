from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class UserPannel(models.Model):
    FIELD_CHOICES = [
        ('ENGINEERING','ENGINEERING'),
        ('MEDICAL','MEDICAL')
    ]
    
    GENDER_CHOICES = [
        ('MALE','MALE'),
        ('FEMALE','FEMALE')
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=False)
    group = models.CharField(max_length=50,choices=FIELD_CHOICES )
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    phone = PhoneNumberField(blank=True,null=True)
    profile_pic = models.ImageField( upload_to="myimage",null=True,blank=True,default='/usericon.png/')
    college = models.CharField(max_length=50)
    programe = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    topic = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    submitted = models.DateTimeField(auto_now_add=True)