from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)