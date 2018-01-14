# oppia_implementations/models.py

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)
    
class OppiaImplementation(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=True)
    lastupdated_date = models.DateTimeField(auto_now=True, editable=True)
    title = models.CharField(max_length=200, blank=False)
    url = models.CharField(max_length=200, unique=True)
    ip = models.GenericIPAddressField(blank=True, default=None, null=True)
    oppia_code_version = models.CharField(max_length=200, blank=True, default=None, null=True)
    server_admin_email = models.CharField(max_length=200, blank=True, default=None, null=True)
    location = models.CharField(max_length=200,blank=True, default=None, null=True)
    description = models.TextField(blank=True, null=True, default=None)
    organisation = models.CharField(max_length=200,blank=True, default=None, null=True)
    organisation_logo = models.FileField(upload_to="organisation_logo",blank=True, default=None)
    organsiation_url = models.CharField(max_length=200,blank=True, default=None, null=True)
    contact_name = models.CharField(max_length=200,blank=True, default=None, null=True)
    contact_email = models.CharField(max_length=200,blank=True, default=None, null=True)
    implementation_logo = models.FileField(upload_to="implementation_logo",blank=True, default=None)
    app_download_url = models.CharField(max_length=200,blank=True, default=None, null=True)
    app_code_url = models.CharField(max_length=200,blank=True, default=None, null=True)
    server_code_url = models.CharField(max_length=200,blank=True, default=None, null=True)
    is_active = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)
    order_by = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = _('Oppia Implementation')
        verbose_name_plural = _('Oppia Implementations')
    
    def __unicode__(self):
        return self.title
    

class ImplementationDataKV(models.Model):
    implementation = models.ForeignKey(OppiaImplementation)
    created_date = models.DateTimeField(auto_now_add=True)
    lastupdated_date = models.DateTimeField(auto_now=True)
    
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
   
    class Meta:
        verbose_name = _('Oppia Implementation Data')
        verbose_name_plural = _('Oppia Implementation Data')
        