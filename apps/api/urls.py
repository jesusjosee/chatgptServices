from django.urls import path
from .views import APiKeyAutenticationView, UploadCSVAPIView


urlpatterns = [
    path('authentication', APiKeyAutenticationView.as_view(), name='authenticationKey'),
    path('uploadcsv', UploadCSVAPIView.as_view(), name='uploadCSV'),
]