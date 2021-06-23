
from django.conf import settings
from django.utils import timezone

from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response

from rest_framework_api_key.permissions import HasAPIKey


from api.serializers import OppiaImplementationSerializer

from oppia_implementations.models import OppiaImplementation, \
                                         ImplementationDataKV
from oppia_implementations import emailer

class OppiaImplementationViewSet(viewsets.ModelViewSet):
    queryset = OppiaImplementation.objects.filter(is_visible=True,
                                                  is_active=True)
    serializer_class = OppiaImplementationSerializer
    permission_classes = [HasAPIKey]
    
    def create(self, request, *args, **kwargs):
        
        imp_data = JSONParser().parse(request)
        imp_url= imp_data['server_url']
        
        try:
            oi = OppiaImplementation.objects.get(url=imp_url)
        except OppiaImplementation.DoesNotExist:
            oi = OppiaImplementation()
            oi.url = imp_url
            # send mail
            emailer.send_oppia_email(
                    template_html='emails/new_site.html',
                    template_text='emails/new_site.txt',
                    subject="New Site registered",
                    fail_silently=False,
                    recipients=[settings.SERVER_EMAIL],
                    new_site_url=imp_url,
                    )
            
        if 'title' in imp_data:
            oi.title = imp_data['title']
            
        oi.save()
        
        if 'email_notifications' in imp_data:
            defaults = { 'value_bool': False }
            ImplementationDataKV.objects.update_or_create(
                    implementation=oi,
                    key=ImplementationDataKV.EMAIL_NOTIFICATIONS,
                    defaults=defaults
                    )
        
        if 'statistics' in imp_data:
            for k, v in imp_data['statistics'].items():
                defaults = { 'value_int': v }
                ImplementationDataKV.objects.update_or_create(
                    implementation=oi,
                    key=k,
                    defaults=defaults
                    )
        
        defaults = { 'value_str': timezone.now() }
        ImplementationDataKV.objects.update_or_create(
            implementation=oi,
            key=ImplementationDataKV.LAST_UPDATE_KEY,
            defaults=defaults
            )
        
        return Response(status=status.HTTP_201_CREATED)
