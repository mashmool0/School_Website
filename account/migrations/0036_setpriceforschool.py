# Generated by Django 5.0.6 on 2024-06-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0035_alter_userstudent_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetPriceForSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_for_rahnamaee', models.PositiveIntegerField()),
                ('price_for_dabirestan', models.PositiveIntegerField()),
            ],
        ),
    ]
