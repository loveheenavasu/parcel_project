# Generated by Django 3.2.6 on 2022-08-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carriers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('rating', models.DecimalField(decimal_places=1, default=None, max_digits=2)),
                ('image_url', models.CharField(max_length=50)),
                ('ratings_amount', models.IntegerField()),
            ],
        ),
    ]
