# Generated by Django 5.0.6 on 2024-06-09 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_basket_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='count',
        ),
    ]
