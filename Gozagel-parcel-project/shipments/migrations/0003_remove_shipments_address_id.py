# Generated by Django 3.2.6 on 2022-08-17 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0002_auto_20220816_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipments',
            name='address_id',
        ),
    ]
