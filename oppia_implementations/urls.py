# oppia_implementations/urls.py
from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView

from oppia_implementations import views as oppia_imp_views

from tastypie.api import Api

v1_api = Api(api_name='v1')
#v1_api.register(TrackerResource())

urlpatterns = [
    url(r'^$', oppia_imp_views.home_view, name="oppia_home"),
    ]