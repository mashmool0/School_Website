# Generated by Django 5.0.6 on 2024-06-03 06:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='last_request_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='otp',
            name='request_count',
            field=models.IntegerField(default=0),
        ),
    ]
