from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import CommonModel

class Account(AbstractUser, CommonModel):
    phone_number = models.CharField(max_length=20)

