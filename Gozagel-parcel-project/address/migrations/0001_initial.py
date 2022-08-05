# Generated by Django 3.2.6 on 2022-08-05 10:36

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
                ('postal_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('federal_tax_id', models.CharField(max_length=50)),
                ('state_tax_id', models.CharField(max_length=50)),
                ('person_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('country_code', models.CharField(default='AD', max_length=2)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.BigIntegerField()),
                ('state_code', models.CharField(max_length=20)),
                ('suburb', models.CharField(max_length=255)),
                ('residential', models.BooleanField(default=False)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(max_length=100)),
                ('validate_location', models.BooleanField(default=False)),
            ],
        ),
    ]
