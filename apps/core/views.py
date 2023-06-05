from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.api.models import ApiKey


# Create your views here.

def home(request):
    apikey = None

    if not isinstance(request.user, AnonymousUser):
        try:
            apikey = ApiKey.objects.filter(user=request.user).last()
        except ApiKey.DoesNotExist:
            pass

    data = {'apikey': apikey}
    
    return render(request, 'core/home.html', data)

    
class ServiceView(TemplateView):
    template_name = "core/service.html"
    


