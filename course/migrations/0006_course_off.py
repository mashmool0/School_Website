# Generated by Django 5.0.6 on 2024-06-08 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='off',
            field=models.CharField(blank=True, help_text='لطفا فقط عدد وارد کنید', max_length=30, null=True, verbose_name='درصد تخفیف'),
        ),
    ]
