# Generated by Django 4.2.5 on 2024-02-12 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0030_rename_time_tablereservation_timein'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablereservation',
            name='additionalrequests',
        ),
    ]