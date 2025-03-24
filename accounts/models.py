from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.email
