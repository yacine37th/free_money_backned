from django.db import models

class Offer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    payout_amount = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField(max_length=200, blank=True)  # Add the URL field

    def __str__(self):
        return self.name
