from django.db import models
class Patient(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    oda_number = models.IntegerField()
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name 