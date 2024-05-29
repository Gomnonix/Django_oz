from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import CommonModel

class Account(AbstractUser, CommonModel):
    phone_number = models.CharField(max_length=20)

# class Account(models.Model): # Model을 상속받는다
# 	name = models.CharField(max_length=20) # 짧은 문장
# 	email = models.CharField(max_length=20) # 긴 텍스트 문장
# 	phone_number = models.CharField(max_length=20)

# 	def __str__(self):
# 		return self.name