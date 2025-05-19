from django.db import models
from django.contrib.auth.models import AbstractUser

USER_ROLES = [
    ('admin', 'Administrator'),
    ('vet', 'Veterinarian'),
    ('recep', 'Receptionist'),
    ('client', 'Client'),
]

SHIFT_CHOICES = [
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
]

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=USER_ROLES, default='client')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class Veterinarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50, unique=True)
    specialty = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.specialty}"

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pet_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.get_full_name()

class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES, default='morning')

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_shift_display()}"
