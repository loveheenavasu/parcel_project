# Generated by Django 3.2.6 on 2022-08-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0003_items_object_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='metadata',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]