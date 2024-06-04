from rest_framework.serializers import ModelSerializer
from .models import Account


class MyInfoAccountSerializer(ModelSerializer):
    class Meta:
      model = Account
      fields = "__all__"
        
    

# Feed에서 노출시킬 User Serializer
# class FeedUserSerializer(ModelSerializer):
#     class Meta:
#         model = User
# 				# fields = "__all__"
#         fields = ("username", "email", "is_superuser")