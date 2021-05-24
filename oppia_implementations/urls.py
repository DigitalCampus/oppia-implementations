# oppia_implementations/urls.py
from django.conf.urls import include, url

from oppia_implementations import views as oppia_imp_views

urlpatterns = [
    url(r'^$', oppia_imp_views.home_view, name="oppia_implementations_home"),
    ]