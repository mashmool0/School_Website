# Generated by Django 5.0.6 on 2024-06-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_remove_otp_last_request_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='id',
        ),
        migrations.AlterField(
            model_name='otp',
            name='phone_number',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
    ]
