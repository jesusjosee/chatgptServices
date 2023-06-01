from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .helpers.autentication import validate_api_key
from .helpers.convert_data import  extract_csv_data

from .models import UploadFile
from .helpers.exceptions import MalformedDataException
# Create your views here.

class APiKeyAutenticationView(APIView):

    def post(self, request, *args, **kwargs):

        api_key = request.data.get("api_key")
        response = validate_api_key(api_key)
        
        if response['api_key'] == 'invalid_api_key':
            return Response({'response': response['api_key']}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({'response': response['api_key']}, status=status.HTTP_200_OK)
      
class UploadCSVAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        
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
