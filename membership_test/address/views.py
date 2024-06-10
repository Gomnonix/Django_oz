from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddressSerializer
from rest_framework.exceptions import NotFound, ParseError
from .models import Address

from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated 

from django.contrib.auth import authenticate, login, logout
from rest_framework import status

import jwt
from django.conf import settings
from config.authentication import JWTAuthentication


class AddressList(APIView):
    #authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]

    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

class AddressDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
        #return Response(serializer.errors, status=status.HTTP_400_BAD_ERROR)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

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

    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username
        })
    

    # "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODcxMTI0NywiaWF0IjoxNzE3NTAxNjQ3LCJqdGkiOiI3NGVjY2RlYTRkZGQ0OGZmODhjYWJiYWVjNDYzYjdmNyIsInVzZXJfaWQiOjF9.9SnZ7pkqFTT8_miKDmVYbJzTIzjN4mUJTcPvcu9rJhs",
    # "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3NTA1MjQ3LCJpYXQiOjE3MTc1MDE2NDcsImp0aSI6ImY1NmU4ZWI2NGMyYzQzMjg4MDhkNjQzOGMzMGIyN2YzIiwidXNlcl9pZCI6MX0.WYL-ktDQ5Dppv0yIexNNdoR3wBSDAQtSiGEXEoOmYVU"
