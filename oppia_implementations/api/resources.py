
import json
import urllib

from django.utils.translation import ugettext_lazy as _

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.exceptions import BadRequest 

from oppia_implementations.models import OppiaImplementation, ImplementationDataKV

class OppiaImplementationResource(ModelResource):
    
    class Meta:
        queryset = OppiaImplementation.objects.all()
        resource_name = 'oppiaimplementation'
        allowed_methods = ['post']
        fields = ['url']
        authorization = Authorization() 
        always_return_data = True 
        include_resource_uri = False
     
 
    def obj_create(self, bundle, **kwargs):
        
        required = ['url']
        for r in required:
            try:
                bundle.data[r]
            except KeyError:
                raise BadRequest(_(u'Please provide your %s') % r)
    
        oi_url = bundle.data['url']

        try: 
            # check url actually exists and is valid Oppia server
            oppia_server_data_test = urllib.urlopen(oi_url + "server/").read()
            
            oppia_server_data = json.loads(oppia_server_data_test)
            oppia_implementation, created = OppiaImplementation.objects.get_or_create(url=oi_url)
            if created:
                oppia_implementation.title = oppia_server_data['name']
            oppia_implementation.oppia_code_version = oppia_server_data['version']
            oppia_implementation.server_admin_email = oppia_server_data['admin_email']
            oppia_implementation.url = oi_url
            oppia_implementation.save()
            
            # add data points if available
            try:
                data_points = bundle.data['data']
                for k,v in data_points.items():
                    data_kv, created = ImplementationDataKV.objects.get_or_create(implementation=oppia_implementation,key=k)
                    data_kv.implementation = oppia_implementation
                    data_kv.key = k
                    data_kv.value = v
                    data_kv.save()
            except KeyError:
                ImplementationDataKV.objects.filter(implementation=oppia_implementation).delete()
            
        except URLError:
            raise BadRequest(_(u'Invalid Oppia server url: %s') % oi_url)
        
        return bundle
