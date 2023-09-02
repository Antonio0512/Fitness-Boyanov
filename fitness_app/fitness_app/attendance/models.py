from django.contrib.auth import get_user_model
from django.db import models
from ..trainer.models import Trainer

User = get_user_model()


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login = models.CharField(max_length=200)
    logout = models.CharField(max_length=200)
    workout = models.CharField(max_length=200)
    trained_by = models.CharField(max_length=200, null=True, blank=True)
