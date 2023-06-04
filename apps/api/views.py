from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from decouple import config
from openai import error as openai_error
from rest_framework.permissions import AllowAny 

from .helpers.autentication import validate_api_key
from .models import UploadFile, ApiKey
from apps.users.models import CustomUser
from .helpers.exceptions import MalformedDataException
from .helpers.convert_data import analize_csv, clean_data_to_array, extract_csv_data
from .helpers.prompts import send_messages_to_chatgpt 

# Create your views here.
class APiKeyAutenticationView(APIView):
    
    def post(self, request, *args, **kwargs):
        
        api_key = request.data.get("api_key")
        response = validate_api_key(api_key)
        
        if response['api_key'] == 'invalid_api_key':
            return Response({'response': response['api_key']}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not isinstance(request.user, AnonymousUser):
            user = get_object_or_404(CustomUser, email=request.user.email)
            ApiKey.objects.create(key=api_key, user=user)
        
        return Response({'response': response['api_key']}, status=status.HTTP_200_OK)
      
class UploadCSVAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        user_text= request.data.get('user-text')
        if user_text:
            #Todo pasarle el texto a chtgpt
            pass
        
        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.endswith('.csv'):
            return Response({'error': 'The file must be in CSV format'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            processed_data = extract_csv_data(file)
            UploadFile.objects.create(csv_file=file)
            return Response({'data': processed_data}, status=status.HTTP_200_OK)
        
        except MalformedDataException:
            return Response({'error': 'The data is malformed or missing data in the rows.'}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AnalizeCSVAPIView(APIView):
    def post(self, request):
        csv_file_path = UploadFile.objects.last()
        # api_key= config("OPENAI_API_KEY2")
        token = self.get_token_from_header(request)
        
        try:
            results = analize_csv(csv_file_path.csv_file)

            res = send_messages_to_chatgpt(results['dataframe'], token)
            
            data = {
                "initial_description" : results["initial_description"],
                "chatgpt_response": clean_data_to_array(res)
            }

            return Response(data, status=status.HTTP_200_OK)
        except openai_error.OpenAIError as e:
            return Response({"error": 'Ocurrió un error al comunicarse con la API de OpenAI:'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_token_from_header(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        
        if authorization_header:
            try:
                auth_type, token = authorization_header.split(' ')
                if auth_type.lower() == 'bearer':
                    return token
            except ValueError:
                pass
        
        return None
