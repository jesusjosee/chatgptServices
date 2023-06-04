from django.shortcuts import render
from django.views.generic import TemplateView
from apps.api.models import ApiKey

# Create your views here.

def home(request):
    apikey = ApiKey.objects.filter(user=request.user)[0]
    data = {}
    if apikey:
        data['apikey'] = apikey
    return render(request, 'core/home.html', data)

# def service(request):
#     return render(request, 'core/service.html')


    
class ServiceView(TemplateView):
    template_name = "core/service.html"
    