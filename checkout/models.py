from django.db import models
from django.contrib.auth.models import User

class CashoutRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_points = models.IntegerField(default=0)  # Representing the requested points
    payment_method = models.CharField(max_length=255)
    payment_address = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
