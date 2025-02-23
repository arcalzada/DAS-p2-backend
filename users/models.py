from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)  # Fecha de nacimiento
    locality = models.CharField(max_length=255, blank=True, null=True)  # Localidad
    municipality = models.CharField(max_length=255, blank=True, null=True)  # Municipio

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )

    def __str__(self):
        return self.username
