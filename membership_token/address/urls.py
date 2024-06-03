from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

# urlpatterns = [
#     path("", views.Addresses.as_view()), 
# 	path("<int:address_id>/address", views.Addresses.as_view())
# ]

urlpatterns = [
path('', views.AddressList.as_view(), name='address-list'),
path('<int:pk>/', views.AddressDetail.as_view(), name='address-detail'),
path('<int:user_id>/add', views.CreateUserAddress.as_view(), name='create-user-address'),
path('<int:pk>/update', views.UpdateAddress.as_view(), name='update-address'),
path('<int:pk>/delete', views.DeleteAddress.as_view(), name='delete-address'),
path("getToken", obtain_auth_token),
]