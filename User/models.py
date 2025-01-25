from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=255)
    Firstname = models.CharField(max_length=255)
    Password = models.TextField(max_length=100)
    Email_address = models.EmailField(max_length=100)
    Phone_number = models.IntegerField()
    Url = models.URLField(max_length=100)
    Date_of_birth = models.DateField(auto_now_add = True)