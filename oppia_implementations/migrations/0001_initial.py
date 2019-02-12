# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImplementationDataKV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('lastupdated_date', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Oppia Implementation Data',
                'verbose_name_plural': 'Oppia Implementation Data',
            },
        ),
        migrations.CreateModel(
            name='OppiaImplementation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('lastupdated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(unique=True, max_length=200)),
                ('ip', models.GenericIPAddressField(default=None, null=True, blank=True)),
                ('oppia_code_version', models.CharField(max_length=200)),
                ('server_admin_email', models.CharField(max_length=200)),
                ('location', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('description', models.TextField(default=None, null=True, blank=True)),
                ('organisation', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('organisation_logo', models.FileField(default=None, upload_to=b'organisation_logo', blank=True)),
                ('organsiation_url', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('contact_name', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('contact_email', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('implementation_logo', models.FileField(default=None, upload_to=b'implementation_logo', blank=True)),
                ('app_download_url', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('app_code_url', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('server_code_url', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('order_by', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Oppia Implementation',
                'verbose_name_plural': 'Oppia Implementations',
            },
        ),
        migrations.AddField(
            model_name='implementationdatakv',
            name='implementation',
            field=models.ForeignKey(to='oppia_implementations.OppiaImplementation', on_delete=models.CASCADE),
        ),
    ]
