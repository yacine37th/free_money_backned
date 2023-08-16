from django.db import models
from django.contrib.auth.models import User

class Offer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    payout_amount = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField(max_length=200, blank=True)  # Add the URL field
    image_url = models.URLField(max_length=200, blank=True)  # Add the URL field

    def __str__(self):
        return self.name


class OfferLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    offer_amount = models.DecimalField(max_digits=10, decimal_places=2)
    log_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.offer.name} - {self.log_date}"