from django.db import models


class MembershipPlan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.IntegerField()
    min_age = models.IntegerField()
    profile_picture = models.ImageField(upload_to="plan_images", null=True, blank=True)

    def __str__(self):
        return self.name