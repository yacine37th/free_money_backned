# Generated by Django 3.1.8 on 2023-08-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
