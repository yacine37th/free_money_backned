from django.db import models

class EmailVerification(models.Model):
    email = models.EmailField(unique=True)
    verification_code = models.CharField(max_length=6)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email