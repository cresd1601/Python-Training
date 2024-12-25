from django_extensions.db.models import TimeStampedModel
from django_softdelete.models import SoftDeleteModel
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, SoftDeleteModel):
    # Custom related_name for avoiding conflict
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="abstract_user_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="abstract_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username


class UserProfile(TimeStampedModel):
    bio = models.TextField(default="This is a default bio.")
    user = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
        related_name="profile",
        primary_key=True,
        serialize=False,
    )

    def __str__(self):
        return f"Profile of {self.user.username}"
