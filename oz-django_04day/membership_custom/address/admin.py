from django.contrib import admin
from .models import Address
from django.contrib.auth.admin import UserAdmin

@admin.register(Address)
class Address(admin.ModelAdmin):
	list_display = ['username', 'street', 'city', 'state', 'postal_code', 'country']
		
