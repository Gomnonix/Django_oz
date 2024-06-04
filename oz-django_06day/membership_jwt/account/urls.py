from django.urls import path
from . import views

urlpatterns = [
	path("<int:account_id>/address", views.Accounts.as_view())
]