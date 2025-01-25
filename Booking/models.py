from django.db import models

# Create your models here.
class Booking(models.Model):
    price = models.FloatField(default='100')
    number_of_guest= models.IntegerField()
    description = models.TextField(default='No description')
    created_at  = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"Booking for {self.number_of_guest} guest(s) at ${self.price}"