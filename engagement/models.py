from django.db import models
from campaigns.models import Campaign


class VolunteerApplication(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    skills = models.TextField()

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE
    )

    applied_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Donation(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    donated_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - ₹{self.amount}"


class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.subject