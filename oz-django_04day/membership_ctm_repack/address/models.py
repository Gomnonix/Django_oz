from django.db import models

class Address(models.Model):
    username = models.CharField(max_length=10)
    street = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=10)


    user = models.ForeignKey("account.Account", on_delete=models.CASCADE, related_name='addresses') # 유저가 데이터가 삭제되면 게시글 데이터도 지운다.  CASCADE
