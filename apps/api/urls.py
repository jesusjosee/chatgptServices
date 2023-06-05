from django.urls import path
from .views import APiKeyAutenticationView, UploadCSVAPIView, AnalizeCSVAPIView, Get_token


urlpatterns = [
    path('authentication', APiKeyAutenticationView.as_view(), name='authenticationKey'),
    path('uploadcsv', UploadCSVAPIView.as_view(), name='uploadCSV'),
    path('analyze-csv', AnalizeCSVAPIView.as_view(), name='analyze_csv'),
    path('token', Get_token.as_view(), name='token'),

]