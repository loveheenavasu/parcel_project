# Generated by Django 3.2.6 on 2022-08-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='paid_by',
            field=models.CharField(choices=[('SENDER', 'sender'), ('RECIPIENT', 'recipient'), ('THIRD_PARTY', 'third_party')], default='sender', max_length=50),
        ),
    ]
