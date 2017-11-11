
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

def home_view(request):
    return render(request, 'oppia_implementations/home.html',  
                              {})