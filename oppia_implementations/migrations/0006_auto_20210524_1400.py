# Generated by Django 2.2.20 on 2021-05-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oppia_implementations', '0005_merge_20190221_0527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='implementationdatakv',
            old_name='value',
            new_name='value_str',
        ),
        migrations.AddField(
            model_name='implementationdatakv',
            name='value_int',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
