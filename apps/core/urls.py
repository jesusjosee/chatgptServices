from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('service', views.ServiceView.as_view(), name='service'),

]