from django.contrib.auth.models import AbstractUser
from django.db import models


class Member(AbstractUser):
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    email = models.EmailField(unique=True, max_length=50)
    phone_number = models.CharField(max_length=12, null=True, blank=True)

    age = models.IntegerField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile_img")

    expiration = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
