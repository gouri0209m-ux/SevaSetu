from django.db import models


class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(
        upload_to='campaigns/',
        blank=True,
        null=True
    )

    location = models.CharField(max_length=100)

    target_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    start_date = models.DateField()

    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        default='Active'
    )

    def __str__(self):
        return self.title