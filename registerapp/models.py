from django.db import models

# Create your models here.
class Registerkoclasshaita(models.Model):
    username_rakha = models.CharField(max_length=40,unique=True)
    email_rakha = models.EmailField(max_length=50,unique=True)
    password_rakha = models.CharField(max_length=40)
    password_thikcha = models.CharField(max_length=50)

