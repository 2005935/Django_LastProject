# Generated by Django 3.1.5 on 2021-11-18 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='site_nae',
            new_name='site_name',
        ),
    ]
