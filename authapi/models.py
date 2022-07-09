from re import M
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

from authapi.options import ROLE_LIST

MAX_LENGTH = 255

class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        """Create user by username and password"""
        if not username:
            raise ValueError('User must have an username!')
        user = self.model(username = username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, password, role):
        """Create superuser by username and password"""
        user = self.create_user(username=username, password=password, role=role)
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""
    USERNAME_FIELD = 'username'
    username = models.CharField(max_length=MAX_LENGTH, unique = True)

    role = models.CharField(choices=ROLE_LIST, max_length=MAX_LENGTH, default="NONE")
    created_at = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"{self.username!r}, {self.role}"
