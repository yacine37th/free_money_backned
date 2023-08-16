from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class CashoutRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_points = models.IntegerField(default=0)  # Representing the requested points
    payment_method = models.CharField(max_length=255)
    payment_address = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class CashOutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cashout_request = models.ForeignKey(CashoutRequest, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user.username} - {self.payment_amount} - {self.payment_date}"
