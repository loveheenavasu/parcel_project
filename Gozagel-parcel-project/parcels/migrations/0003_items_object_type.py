# Generated by Django 3.2.6 on 2022-08-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0002_rename_items_id_items_parcel_items_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='object_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]