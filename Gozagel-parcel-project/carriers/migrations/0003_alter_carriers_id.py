# Generated by Django 3.2.6 on 2022-05-24 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carriers', '0002_auto_20220302_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carriers',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
