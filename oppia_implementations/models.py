# oppia_implementations/models.py

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)
    
class OppiaImplementation(models.Model):
    created_date = models.DateTimeField('date created',default=timezone.now)
    lastupdated_date = models.DateTimeField('date updated',default=timezone.now)
    title = models.TextField(blank=False)
    url = models.CharField(max_length=200)
    ip = models.GenericIPAddressField()
    oppia_code_version = models.CharField(max_length=200)
    server_admin_email = models.CharField(max_length=200)
    location = models.CharField(max_length=200,blank=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    organisation = models.CharField(max_length=200,blank=True, default=None)
    organisation_logo = models.FileField(upload_to="organisation_logo",blank=True, default=None)
    organsiation_url = models.CharField(max_length=200,blank=True, default=None)
    contact_name = models.CharField(max_length=200,blank=True, default=None)
    contact_email = models.CharField(max_length=200,blank=True, default=None)
    implementation_logo = models.FileField(upload_to="implementation_logo",blank=True, default=None)
    app_download_url = models.CharField(max_length=200,blank=True, default=None)
   
    class Meta:
        verbose_name = _('Oppia Implementation')
        verbose_name_plural = _('Oppia Implementations')
        
    def __unicode__(self):
        return self.title(self)
    

class ImplementationDataKV(models.Model):
    implementations = models.ForeignKey(OppiaImplementation)
    created_date = models.DateTimeField('date created',default=timezone.now)
    lastupdated_date = models.DateTimeField('date updated',default=timezone.now)
    
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
   
    class Meta:
        verbose_name = _('Oppia Implementation Data')
        verbose_name_plural = _('Oppia Implementation Data')
        
    def __unicode__(self):
        return self.name(self)