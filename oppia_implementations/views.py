
from django.shortcuts import render

from oppia_implementations.models import OppiaImplementation

def home_view(request):
    implementations = OppiaImplementation.objects.filter(
        is_visible=True, is_active=True).order_by('-order_by', 'title')
    prev_imp = OppiaImplementation.objects.filter(
        is_visible=True, is_active=False).order_by('-order_by', 'title')
    return render(request, 'oppia_implementations/home.html',  
                              {'implementations': implementations,
                               'previous_implementations': prev_imp})