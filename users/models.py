from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    details = models.CharField(max_length=320, null=True, blank=True)
