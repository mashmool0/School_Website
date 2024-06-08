from django.db import models


# Create your models here.
class Course(models.Model):
    COURSE_TYPE_CHOICES = [
        ('book', 'کتاب'),
        ('teacher', 'آموزش'),
    ]
    course_name = models.CharField(max_length=30, verbose_name="نام دوره")
    price = models.CharField(max_length=20, verbose_name="قیمت دوره",
                             help_text="حتما قیمت دوره را به تومان و بدون هیچ علائم نگارشی اضافه ای وارد کنید ")
    teacher = models.CharField(max_length=30, verbose_name="استاد دوره",
                               help_text="فقط اسم و فامیل استاد را بنویسید نیاز به نوشتن کلمه استاد قبل از اسم اساتید "
                                         "نیست ")
    date_starter = models.DateField(verbose_name="روز شروع دوره",
                                    help_text="اگر روز شروع خاصی مد نظرتون نیست یا شروع خاصی ندارد تاریخ امروز را "
                                              "وارد کنید")
    banner = models.ImageField(upload_to='media/', default=True, verbose_name="عکس دوره")
    course_type = models.CharField(max_length=30, choices=COURSE_TYPE_CHOICES, verbose_name="نوع دوره")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره ها"
