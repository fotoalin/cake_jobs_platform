# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# from courses.models import Course
# from jobs.models import Job


class CustomUser(AbstractUser):
    is_decorator = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_subscriber = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",  # Change the related name to avoid conflicts
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",  # Change the related name to avoid conflicts
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
