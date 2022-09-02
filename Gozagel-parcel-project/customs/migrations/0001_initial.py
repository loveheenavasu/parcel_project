# Generated by Django 3.2.6 on 2022-09-01 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodities_id', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.IntegerField()),
                ('weight_unit', models.CharField(max_length=2)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('value_amount', models.IntegerField(blank=True, null=True)),
                ('value_currency', models.CharField(blank=True, max_length=3, null=True)),
                ('origin_country', models.CharField(blank=True, max_length=3, null=True)),
                ('parent_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Custom_Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aes', models.CharField(max_length=255)),
                ('eel_pfc', models.CharField(max_length=255)),
                ('license_number', models.CharField(max_length=255)),
                ('certificate_number', models.CharField(max_length=255)),
                ('nip_number', models.CharField(max_length=255)),
                ('eori_number', models.CharField(max_length=255)),
                ('vat_registration_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duty_id', models.CharField(blank=True, max_length=255, null=True)),
                ('paid_by', models.CharField(choices=[('SENDER', 'sender'), ('RECIPIENT', 'recipient'), ('THIRD_PARTY', 'third_party')], default='sender', max_length=50)),
                ('currency', models.CharField(blank=True, max_length=3, null=True)),
                ('declared_value', models.IntegerField(blank=True, null=True)),
                ('account_number', models.CharField(blank=True, max_length=250, null=True)),
                ('bill_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.address')),
            ],
        ),
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Custom_id', models.CharField(max_length=255, null=True)),
                ('content_type', models.CharField(blank=True, max_length=250, null=True)),
                ('content_description', models.CharField(blank=True, max_length=250, null=True)),
                ('incoterm', models.CharField(blank=True, max_length=3, null=True)),
                ('invoice', models.CharField(blank=True, max_length=50, null=True)),
                ('invoice_date', models.CharField(blank=True, max_length=250, null=True)),
                ('commercial_invoice', models.BooleanField(blank=True, null=True)),
                ('certify', models.BooleanField(blank=True, null=True)),
                ('signer', models.CharField(blank=True, max_length=50, null=True)),
                ('commodities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customs.commodities')),
                ('duty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customs.duty')),
                ('options', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customs.custom_options')),
            ],
        ),
    ]
