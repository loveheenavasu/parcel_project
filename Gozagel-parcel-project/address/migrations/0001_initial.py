# Generated by Django 3.2.6 on 2022-08-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_id', models.CharField(max_length=255)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('federal_tax_id', models.CharField(blank=True, max_length=50, null=True)),
                ('state_tax_id', models.CharField(blank=True, max_length=50, null=True)),
                ('person_name', models.CharField(blank=True, max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('country_code', models.CharField(default='AD', max_length=2)),
                ('email', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('state_code', models.CharField(blank=True, max_length=20, null=True)),
                ('suburb', models.CharField(blank=True, max_length=255, null=True)),
                ('residential', models.BooleanField(blank=True, default=False, null=True)),
                ('address_line1', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('validate_location', models.BooleanField(default=False)),
            ],
        ),
    ]
