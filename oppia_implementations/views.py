import time

from django.http import JsonResponse
from django.shortcuts import render

from rest_framework_api_key.models import APIKey

from oppia_implementations.models import OppiaImplementation


def home_view(request):
    implementations = OppiaImplementation.objects.filter(
        is_visible=True, is_active=True).order_by('-order_by', 'title')
    prev_imp = OppiaImplementation.objects.filter(
        is_visible=True, is_active=False).order_by('-order_by', 'title')
    return render(request, 'oppia_implementations/home.html',  
                              {'implementations': implementations,
                               'previous_implementations': prev_imp})
   
def get_api_key_view(request):
    api_key, key = APIKey.objects.create_key(name=time.time())
    json_data = {'key': key}
    return JsonResponse(json_data)
