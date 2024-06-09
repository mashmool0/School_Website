# Generated by Django 5.0.6 on 2024-06-08 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_course_off_alter_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='off',
            field=models.IntegerField(blank=True, help_text='لطفا فقط عدد وارد کنید', null=True, verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(help_text='حتما قیمت دوره را به تومان و بدون هیچ علائم نگارشی اضافه ای وارد کنید ', verbose_name='قیمت دوره'),
        ),
    ]