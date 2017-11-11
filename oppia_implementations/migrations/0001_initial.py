# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImplementationDataKV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created')),
                ('lastupdated_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date updated')),
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
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created')),
                ('lastupdated_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date updated')),
                ('title', models.TextField()),
                ('url', models.CharField(max_length=200)),
                ('ip', models.GenericIPAddressField()),
                ('oppia_code_version', models.CharField(max_length=200)),
                ('server_admin_email', models.CharField(max_length=200)),
                ('location', models.CharField(default=None, max_length=200, blank=True)),
                ('description', models.TextField(default=None, null=True, blank=True)),
                ('organisation', models.CharField(default=None, max_length=200, blank=True)),
                ('organisation_logo', models.FileField(default=None, upload_to=b'organisation_logo', blank=True)),
                ('organsiation_url', models.CharField(default=None, max_length=200, blank=True)),
                ('contact_name', models.CharField(default=None, max_length=200, blank=True)),
                ('contact_email', models.CharField(default=None, max_length=200, blank=True)),
                ('implementation_logo', models.FileField(default=None, upload_to=b'implementation_logo', blank=True)),
                ('app_download_url', models.CharField(default=None, max_length=200, blank=True)),
            ],
            options={
                'verbose_name': 'Oppia Implementation',
                'verbose_name_plural': 'Oppia Implementations',
            },
        ),
        migrations.AddField(
            model_name='implementationdatakv',
            name='implementations',
            field=models.ForeignKey(to='oppia_implementations.OppiaImplementation'),
        ),
    ]
