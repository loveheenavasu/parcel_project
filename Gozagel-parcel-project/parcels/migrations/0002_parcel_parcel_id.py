# Generated by Django 3.2.6 on 2022-08-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='parcel_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]