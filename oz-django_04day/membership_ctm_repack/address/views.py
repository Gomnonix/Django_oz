from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddressSerializer
from .models import Address
from django.shortcuts import get_object_or_404


class AddressList(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)
    
    def get_object(self, user_id):
        return get_object_or_404(Address, user_id=user_id)
    
    # def post(self, request, user_id): 
    #     serializer = AddressSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user_id=user_id)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_ERROR)
    # URL에서 user_id를 가져와서 사용한다.
    
    def post(self, request):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddressDetail(APIView):
    def get_object(self, user_id):
        return get_object_or_404(Address, user_id=user_id)

    def get(self, request, user_id):
        address = self.get_object(user_id)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AddressSerializer(address)
        return Response(serializer.data)
    
    def put(self, request, user_id):
        address = self.get_object(user_id)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id):
        address = self.get_object(user_id)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class CreateUserAddress(APIView):
#     def post(self, request, user_id):
#         serializer = AddressSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user_id=user_id)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_ERROR)
        
