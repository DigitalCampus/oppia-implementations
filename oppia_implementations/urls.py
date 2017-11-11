# oppia_implementations/urls.py
from django.conf.urls import url

from oppia_implementations import views as oppia_imp_views

from tastypie.api import Api

v1_api = Api(api_name='v1')
#v1_api.register(TrackerResource())

urlpatterns = [
    url(r'^$', oppia_imp_views.home_view, name="oppia_implementations_home"),
    ]