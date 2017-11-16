# oppia_implementations/urls.py
from django.conf.urls import include, url

from oppia_implementations import views as oppia_imp_views
from oppia_implementations.api.resources import OppiaImplementationResource

from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(OppiaImplementationResource())

urlpatterns = [
    url(r'^$', oppia_imp_views.home_view, name="oppia_implementations_home"),
    
    url(r'^api/', include(v1_api.urls)),
    
    ]