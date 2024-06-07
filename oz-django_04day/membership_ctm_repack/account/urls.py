from django.urls import path
from . import views

urlpatterns = [
	path('', views.Accounts.as_view())
]