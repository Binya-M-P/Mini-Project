# Generated by Django 4.2.5 on 2023-11-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0023_cart_ready_to_deliver'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ready_to_deliver',
            field=models.BooleanField(default=False),
        ),
    ]
