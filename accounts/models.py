from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [ 
        ('customer', 'Customer'),
        ('staff', 'Staff'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='customer'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
