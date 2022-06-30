from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manager import AccountManager


class User(AbstractBaseUser, PermissionsMixin):
    '''Custom User Model'''
    username = models.CharField(max_length=40, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
