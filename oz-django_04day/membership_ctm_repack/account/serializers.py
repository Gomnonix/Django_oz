from rest_framework.serializers import ModelSerializer
from .models import Account


class MyInfoAccountSerializer(ModelSerializer):
    class Meta:
      model = Account
      fields = "__all__"
        