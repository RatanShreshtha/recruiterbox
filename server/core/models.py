from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from kudos.models import Kudo
from datetime import datetime



class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    organization = models.ForeignKey(
        "Organization", on_delete=models.CASCADE, null=True, blank=True
    )

    def kudos(self):
        month_starting = datetime.today().replace(
            day=1, hour=0, minute=0, second=0, microsecond=0
        )
        kudos_this_month = (
            Kudo.objects.filter(by_user=self)
            .filter(awarded__gte=month_starting)
            .count()
        )
        return settings.KUDOS_MONTHLY_QUOTA - kudos_this_month

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
