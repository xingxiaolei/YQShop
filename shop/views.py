from django.shortcuts import render
from django.conf import settings
from shop.models import Banner
from django.views import View

def global_settings(request):
    return {
        'MEDIA_URL': settings.MEDIA_URL
    }


class Index(View):
    def get(self,request):
        bann = Banner.objects.all()


        context = {
            'bann': bann
        }

        return render(request, 'index.html')

