from django.contrib.auth.models import (AbstractUser, BaseUserManager)
from django.db import models


class User(AbstractUser):
  email = models.EmailField(unique=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []