from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)


class Company(models.Model):
    СOMPANY_TYPES = (
        ('IP', 'ИП'),
        ('TOO', 'ТОО'),
        ('AO', 'АО'),
    )

    name = models.CharField(max_length=100)
    company_type = models.CharField(
        max_length=3,
        choices=СOMPANY_TYPES,
    )
    date_creation = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    FEEDBACK_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    text = models.TextField()
    star = models.CharField(choices=FEEDBACK_CHOICES, max_length=1)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
