from django.db import models

class Card(models.Model):
    CARD_TYPES = [
        ('PayPal', 'PayPal'),
        ('Amazon Gift Card', 'Amazon Gift Card'),
        ('Payeer', 'Payeer'),
        ('Visa Card', 'Visa Card'),
        # Add more card types as needed
    ]

    card_type = models.CharField(max_length=255, choices=CARD_TYPES)
    points_required = models.IntegerField()  # Points required to redeem this card
    image = models.ImageField(upload_to='cards/')
    description = models.TextField()

    def __str__(self):
        return f"{self.card_type} Card"
