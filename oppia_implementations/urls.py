# oppia_implementations/urls.py
from django.urls import include, path

from oppia_implementations import views

urlpatterns = [
    path('', views.home_view, name="oppia_implementations_home"),
    path('get-api-key/', views.get_api_key_view, name="get_api_key"),
    path('api/', include('api.urls')),
    ]
