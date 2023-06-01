import requests
from decouple import config

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .autentication import validate_api_key

# Create your views here.

class APiKeyAutenticationView(APIView):

    def post(self, request, *args, **kwargs):

        api_key = request.data.get("api_key")
        response = validate_api_key(api_key)
        
        if response['api_key'] == 'invalid_api_key':
            return Response({'response': response['api_key']}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({'response': response['api_key']}, status=status.HTTP_200_OK)
      
