from django.urls import path
from .views import APiKeyAutenticationView


urlpatterns = [
    path('authentication', APiKeyAutenticationView.as_view(), name='authenticationKey'),
]