from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

@admin.register(Account)
class Account(UserAdmin): #useradmin을 상속받기때문에 모델이 users로 나오는 것이다.
	list_display = ['username', 'email', 'phone_number', "created_at", "updated_at",]
		# list_filter= ["name", "phone_number"]

# admin.site.register(Account)