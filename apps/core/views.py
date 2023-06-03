from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

# def service(request):
#     return render(request, 'core/service.html')


    
class ServiceView(TemplateView):
    template_name = "core/service.html"
    