from django.shortcuts import render
from django.views import View
from django.conf import settings

# Create your views here.

class HomeView(View):
    def get(self, request):
        
        # Procesar la solicitud
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'app_name': settings.APP_NAME,
            'app_version': settings.APP_VERSION,
            
        }
        print(f"Application: {context.get('app_name')} - {context.get('app_version')}")
        return render(request, 'home/index.html', context)