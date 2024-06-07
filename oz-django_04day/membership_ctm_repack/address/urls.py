from django.urls import path
from . import views

urlpatterns = [
path('', views.AddressList.as_view(), name='address-list'),
path('/<int:user_id>/', views.AddressDetail.as_view(), name='address-detail'),

#path('/<int:user_id>/add', views.CreateUserAddress.as_view(), name='create-user-address'),
#path('/<int:user_id>/update', views.UpdateAddress.as_view(), name='update-address'),
#path('/<int:user_id>/delete', views.DeleteAddress.as_view(), name='delete-address'),
]