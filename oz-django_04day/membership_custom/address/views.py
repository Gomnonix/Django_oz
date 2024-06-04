from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddressSerializer
from .models import Address


# class Addresses(APIView):
# 	def get(self, request):
# 		addresses = Address.objects.all() 
# 		serializer = AddressSerializer(addresses, many=True) 
# 		return Response(serializer.data)
	
# 	def post(self, request):
# 		serializer = AddressSerializer(data=request.data)
# 		if serializer.is_valid():
# 			address = serializer.save(user=request.user)
# 			serializer = AddressSerializer(address)
# 			return Response(serializer.data)
# 		else:
# 			return Response(serializer.errors)
	
# 	def put(self, request, address_id):
# 		address = Address.objects.get(id=address_id)
# 		serializer = AddressSerializer(address, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors)
	
# 	def delete(self, request, address_id):
# 		address = Address.objects.get(id=address_id)
# 		address.delete()
# 		return Response(status=200)

class AddressList(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

class AddressDetail(APIView):
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return None
    def get(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AddressSerializer(address)
        return Response(serializer.data)
        
class CreateUserAddress(APIView):
    def post(self, request, user_id):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_ERROR)

class UpdateAddress(APIView):
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return None

    def put(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # 데이터 업데이트 부분에서 request.data를 직접 사용
        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteAddress(APIView):
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return None
    def delete(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
