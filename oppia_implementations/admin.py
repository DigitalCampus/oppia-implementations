# oppia_implementations/admin.py
from django.contrib import admin

from oppia_implementations.models import OppiaImplementation, ImplementationDataKV

class OppiaImplementationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'organisation', 'location', 'oppia_code_version', 'is_active', 'is_visible')
    
class ImplementationDataKVAdmin(admin.ModelAdmin):
    list_display = ('implementation', 'key', 'value' )
    
    
admin.site.register(OppiaImplementation, OppiaImplementationsAdmin) 
admin.site.register(ImplementationDataKV, ImplementationDataKVAdmin) 