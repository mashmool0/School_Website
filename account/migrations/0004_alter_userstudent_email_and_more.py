# Generated by Django 5.0.6 on 2024-05-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_welcomeregister_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstudent',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='userstudent',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
