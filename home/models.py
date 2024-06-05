from django.db import models


# Create your models here.

class Course(models.Model):
    COURSE_TYPE_CHOICES = [
        ('book', 'کتاب'),
        ('teacher', 'آموزش'),
    ]
    course_name = models.CharField(max_length=30, verbose_name="نام دوره")
    price = models.CharField(max_length=20, verbose_name="قیمت دوره")
    teacher = models.CharField(max_length=30, verbose_name="استاد دوره")
    date_starter = models.DateField(verbose_name="روز شروع دوره")
    banner = models.ImageField(upload_to='media/', verbose_name="عکس دوره")
    course_type = models.CharField(max_length=30, choices=COURSE_TYPE_CHOICES, verbose_name="نوع دوره")

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره ها"
