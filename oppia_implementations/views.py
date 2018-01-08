
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from oppia_implementations.models import OppiaImplementation, ImplementationDataKV

def home_view(request):
    implementations = OppiaImplementation.objects.filter(is_visible=True).order_by('-order_by', 'title')
    return render(request, 'oppia_implementations/home.html',  
                              {'implementations': implementations})