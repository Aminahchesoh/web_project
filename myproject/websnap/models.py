from django.db import models

# Create your models here.

class Messages (models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    messages = models.CharField(max_length=500)

def __str__(self):
    return f"{self.firstname} {self.lastname}"

