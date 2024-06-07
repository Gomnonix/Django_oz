from rest_framework.serializers import ModelSerializer # 모델 인스턴스를 자동으로 직렬화하거나 역직렬화할 수 있다.
from .models import Address

class AddressSerializer(ModelSerializer):
    class Meta: # 모델이나 직렬화기에서 메타데이터를 정의하는 데 사용, ModelSerializer에서 어떤 모델을 사용할지 지정
        model = Address
        fields = "__all__"

