# Generated by Django 3.1.5 on 2021-11-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_nae', models.CharField(max_length=100)),
                ('url', models.URLField(verbose_name='Site URL')),
            ],
        ),
    ]