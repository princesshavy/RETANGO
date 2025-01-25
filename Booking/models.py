from django.db import models

# Create your models here.
class Booking(models.Model):
    Price = models.FloatField(max_length=255)
    Number_of_guest= models.IntegerField(max_length=100)
    Description = models.TextField(max_length=100)
    DateTime_of_booking = models.DateTimeField(auto_now_add=True)
