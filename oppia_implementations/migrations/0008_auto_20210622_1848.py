# Generated by Django 2.2.24 on 2021-06-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oppia_implementations', '0007_implementationdatakv_value_bool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='implementationdatakv',
            name='value_str',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
