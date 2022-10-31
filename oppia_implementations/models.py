# oppia_implementations/models.py

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

    
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
    organisation_url = models.CharField(max_length=200,blank=True, default=None, null=True)
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
    
    def __str__(self):
        return self.title
    

class ImplementationDataKV(models.Model):
    
    LAST_UPDATE_KEY = "LAST_UPDATED"
    NO_COURSES_KEY = "NO_COURSES"
    NO_USERS_KEY = "NO_USERS"
    EMAIL_NOTIFICATIONS = "EMAIL_NOTIFICATIONS"
    EMAIL_NOTIF_ADDRESS = "EMAIL_NOTIF_ADDRESS"
    
    implementation = models.ForeignKey(OppiaImplementation, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    lastupdated_date = models.DateTimeField(auto_now=True)
    
    key = models.CharField(max_length=200)
    value_str = models.CharField(max_length=200, blank=True, default=None, null=True)
    value_int = models.IntegerField(blank=True, default=None, null=True)
    value_bool = models.BooleanField(blank=True, null=True)
    is_visible = models.BooleanField(default=False)
   
    class Meta:
        verbose_name = _('Oppia Implementation Data')
        verbose_name_plural = _('Oppia Implementation Data')
        
    @staticmethod
    def get_property(property_key, default_value):
        try:
            prop = ImplementationDataKV.objects.get(key=property_key)
            value = None
            if prop.str_value is not None:
                value = prop.str_value
            elif prop.int_value is not None:
                value = prop.int_value
            elif prop.bool_value is not None:
                value = prop.bool_value
            if value is not None:
                return value
        except ImplementationDataKV.DoesNotExist:
            pass

        return default_value

    @staticmethod
    def get_int(property_key, default_value):
        try:
            prop = ImplementationDataKV.objects.get(key=property_key)
            if prop.int_value is not None:
                return prop.int_value
        except ImplementationDataKV.DoesNotExist:
            pass
        return default_value

    @staticmethod
    def get_string(property_key, default_value):
        try:
            prop = ImplementationDataKV.objects.get(key=property_key)
            if prop.str_value is not None:
                return prop.str_value
        except ImplementationDataKV.DoesNotExist:
            pass
        return default_value

    @staticmethod
    def get_bool(property_key, default_value):
        try:
            prop = ImplementationDataKV.objects.get(key=property_key)
            if prop.bool_value is not None:
                return prop.bool_value
        except ImplementationDataKV.DoesNotExist:
            pass
        return default_value

    @staticmethod
    def set_int(property_key, value):
        prop, created = ImplementationDataKV.objects \
            .get_or_create(key=property_key)
        prop.int_value = value
        prop.save()

    @staticmethod
    def set_string(property_key, value):
        prop, created = ImplementationDataKV.objects \
            .get_or_create(key=property_key)
        prop.str_value = value
        prop.save()

    @staticmethod
    def set_bool(property_key, value):
        prop, created = ImplementationDataKV.objects \
            .get_or_create(key=property_key)
        prop.bool_value = value
        prop.save()

    @staticmethod
    def delete_key(property_key):
        ImplementationDataKV.objects.get(key=property_key).delete()

    def __str__(self):
        return self.key
        