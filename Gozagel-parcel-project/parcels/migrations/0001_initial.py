# Generated by Django 3.2.6 on 2022-08-10 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_id', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.IntegerField()),
                ('weight_unit', models.CharField(max_length=2)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('value_amount', models.IntegerField(blank=True, null=True)),
                ('value_currency', models.CharField(blank=True, max_length=3, null=True)),
                ('origin_country', models.CharField(blank=True, max_length=3, null=True)),
                ('parent_id', models.CharField(blank=True, max_length=255, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Items_metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(blank=True, max_length=255, null=True)),
                ('reference1', models.CharField(blank=True, max_length=255, null=True)),
                ('reference2', models.CharField(blank=True, max_length=255, null=True)),
                ('reference3', models.CharField(blank=True, max_length=255, null=True)),
                ('reference4', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='parcel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('length', models.IntegerField(default=0)),
                ('packaging_type', models.CharField(blank=True, max_length=50, null=True)),
                ('package_preset', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.CharField(blank=True, max_length=100, null=True)),
                ('is_document', models.BooleanField(default=False)),
                ('dimension_unit', models.CharField(max_length=10)),
                ('weight', models.IntegerField()),
                ('weight_unit', models.CharField(max_length=2)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('value_amount', models.IntegerField(blank=True, null=True)),
                ('value_currency', models.CharField(blank=True, max_length=3, null=True)),
                ('origin_country', models.CharField(blank=True, max_length=3, null=True)),
                ('parent_id', models.CharField(blank=True, max_length=255, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=100, null=True)),
                ('metadata', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel_id', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('length', models.IntegerField(default=0)),
                ('packaging_type', models.CharField(blank=True, max_length=50, null=True)),
                ('package_preset', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('content', models.CharField(blank=True, max_length=100, null=True)),
                ('is_document', models.BooleanField(default=False)),
                ('weight_unit', models.CharField(blank=True, max_length=2, null=True)),
                ('dimension_unit', models.CharField(max_length=10)),
                ('reference_number', models.CharField(blank=True, max_length=100, null=True)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcels.items')),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='metadata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcels.items_metadata'),
        ),
    ]
