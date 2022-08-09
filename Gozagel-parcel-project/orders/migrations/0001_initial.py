# Generated by Django 3.2.6 on 2022-08-09 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipments', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=222)),
                ('last_name', models.CharField(max_length=222)),
                ('email', models.EmailField(max_length=254)),
                ('Parcel_contents', models.CharField(max_length=250)),
                ('pracel_value', models.CharField(max_length=222)),
                ('sender_first_name', models.CharField(max_length=222)),
                ('sender_last_name', models.CharField(max_length=222)),
                ('sender_mail', models.EmailField(max_length=254)),
                ('sender_company', models.CharField(max_length=222)),
                ('sender_vat_number', models.CharField(max_length=222)),
                ('address', models.CharField(max_length=255)),
                ('sender_apartment', models.CharField(max_length=222)),
                ('city', models.CharField(max_length=255)),
                ('sender_county', models.CharField(max_length=222, null=True)),
                ('sender_province', models.CharField(max_length=222)),
                ('postal_code', models.CharField(max_length=222)),
                ('sender_Phone', models.CharField(max_length=222)),
                ('recipient_first_name', models.CharField(max_length=255)),
                ('recipient_last_name', models.CharField(max_length=255)),
                ('recipient_email', models.EmailField(max_length=254)),
                ('recipient_company', models.CharField(max_length=222)),
                ('recipient_vat_number', models.CharField(max_length=222)),
                ('recipient_address', models.CharField(max_length=255)),
                ('recipient_apartment', models.CharField(max_length=222)),
                ('recipient_city', models.CharField(max_length=255)),
                ('recipient_country', models.CharField(max_length=222, null=True)),
                ('recipient_province', models.CharField(max_length=222)),
                ('recipient_postal_code', models.CharField(max_length=222)),
                ('recipient_phone', models.CharField(max_length=222)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Payment Status')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('stripe_payment_intent', models.CharField(max_length=200, verbose_name='Payment Intent')),
                ('shipment_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='shipments.shipments')),
                ('user_id', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]