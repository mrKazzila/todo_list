from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)
