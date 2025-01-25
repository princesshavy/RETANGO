from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    password = models.CharField(max_length=100, default='12345')
    email_address = models.EmailField(max_length=100, unique=True, default='hvh@gmail.com')
    phone_number = models.CharField(max_length=15, default='1234567890')
    date_of_birth = models.DateField(default=datetime.date(2025, 1, 12))
    profile_picture = models.ImageField(upload_to='user/profile_image', default='user/profile_image/default.jpg')

    def __str__(self):
        return self.username