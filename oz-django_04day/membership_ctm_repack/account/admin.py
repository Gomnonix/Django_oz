from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

@admin.register(Account)
class Account(UserAdmin):
	list_display = ['username', 'email', 'phone_number', "created_at", "updated_at",]
		# list_filter= ["name", "phone_number"]