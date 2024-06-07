from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MyInfoAccountSerializer
from .models import Account


class Accounts(APIView):
	def get(self, request): 
		user = Account.objects.all() 
		serializer = MyInfoAccountSerializer(user, many=True) 
		return Response(serializer.data)
	
	def post(self, request):
		serializer = MyInfoAccountSerializer(data=request.data)
		if serializer.is_valid(): 
			user = serializer.save(user=request.user)
			serializer = MyInfoAccountSerializer(user)
			return Response(serializer.data)
		else:
			return Response(serializer.errors)
      
