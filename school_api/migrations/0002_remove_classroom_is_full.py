# Generated by Django 3.0 on 2020-08-01 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='is_full',
        ),
    ]
