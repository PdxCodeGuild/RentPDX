from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):

    #defining the two choices for user types, selected in forms
    user_type_choices = [
        ('homeowner', 'owner'),
        ('homerenter', 'renter'),
    ]
    user_type = models.CharField(choices=user_type_choices, blank=True, null=True, max_length=20)

    birthdate = models.DateField(blank=False, null=True)

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    
    #method to determine full name by combining first and last name
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.username


