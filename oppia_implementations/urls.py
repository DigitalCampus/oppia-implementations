# oppia_implementations/urls.py
from django.conf.urls import include, url
from django.urls import path

from oppia_implementations import views

urlpatterns = [
    url(r'^$', views.home_view, name="oppia_implementations_home"),
    url(r'^get-api-key/$', views.get_api_key_view, name="get_api_key"),
    path(r'api/', include('api.urls')),
    ]