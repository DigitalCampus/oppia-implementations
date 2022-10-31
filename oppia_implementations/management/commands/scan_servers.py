# coding: utf-8

"""
Management command to scan Oppia servers to get up to date info
"""
import urllib
import json 
import os
import time 
import django.db.models

from optparse import make_option

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from oppia_implementations.models import OppiaImplementation, ImplementationDataKV


class BColors:
    HEADER = '\033[95m'
    OK = '\033[92m'
    WARNING = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


class Command(BaseCommand):
    help = _(u"Scans Oppia servers to get up to date info")        

    def handle(self, *args, **options):
        implementations = OppiaImplementation.objects.filter(is_active=True)
        for implementation in implementations:
            print(_(u'Checking: %s' % implementation.url))
            url = '%sserver/' % (implementation.url)
            try:
                u = urllib.request.urlopen(url, timeout=10)
                data = u.read()  
                datajson = json.loads(data)
                
                # check version no
                if implementation.oppia_code_version != datajson['version']:
                    update = input(_(u"%sVersion from server (%s) doesn't match the one stored (%s).%s Update [y/n]?" % (BColors.WARNING, datajson['version'], implementation.oppia_code_version, BColors.ENDC)))
                    if update == 'y' :
                        implementation.oppia_code_version = datajson['version']
                        implementation.save()
                        print(_(u'Updated'))
                        
                # check admin email
                if implementation.server_admin_email != datajson['admin_email']:
                    update = input(_(u"%sAdmin email from server (%s) doesn't match the one stored (%s).%s Update [y/n]?" % (BColors.WARNING, datajson['admin_email'], implementation.server_admin_email, BColors.ENDC)))
                    if update == 'y' :
                        implementation.server_admin_email = datajson['admin_email']
                        implementation.save()
                        print(_(u'Updated'))
                
                
            except ValueError:
                print(_(u"%sServer data not found%s" % (BColors.WARNING, BColors.ENDC)))
            except urllib.error.URLError:
                print(_(u"%sServer unreachable%s" % (BColors.WARNING, BColors.ENDC)))
                
            # update last scan date
            lastupdate, created = ImplementationDataKV.objects.get_or_create(
                implementation=implementation,
                key=ImplementationDataKV.LAST_UPDATE_KEY)   
            lastupdate.value_str = timezone.now()
            lastupdate.save()
            