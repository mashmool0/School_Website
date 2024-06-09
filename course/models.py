from django.db import models


# Create your models here.
class Course(models.Model):
    COURSE_TYPE_CHOICES = [
        ('book', 'کتاب'),
        ('teacher', 'آموزش'),
    ]
    course_name = models.CharField(max_length=30, verbose_name="نام دوره")
    price = models.IntegerField(verbose_name="قیمت دوره",
                                help_text="حتما قیمت دوره را به تومان و بدون هیچ علائم نگارشی اضافه ای وارد کنید ")
    teacher = models.CharField(max_length=30, verbose_name="استاد دوره",
                               help_text="فقط اسم و فامیل استاد را بنویسید نیاز به نوشتن کلمه استاد قبل از اسم اساتید "
                                         "نیست ")
    date_starter = models.DateField(verbose_name="روز شروع دوره",
                                    help_text="اگر روز شروع خاصی مد نظرتون نیست یا شروع خاصی ندارد تاریخ امروز را "
                                              "وارد کنید")
    banner = models.ImageField(upload_to='media/', verbose_name="عکس دوره")
    course_type = models.CharField(max_length=30, choices=COURSE_TYPE_CHOICES, verbose_name="نوع دوره")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    off = models.IntegerField(null=True, blank=True, verbose_name="درصد تخفیف",
                              help_text="لطفا فقط عدد وارد کنید،لطفا عدد وارد شده بین 1 تا 100 باشد")
    price_with_off = models.IntegerField(null=True, blank=True, verbose_name="قیمت با تخفیف ")

    def __str__(self):
        return self.course_name

    def set_price_with_off(self):
        if self.off is not None:
            self.price_with_off = (self.price * (100 - self.off)) / 100
        else:
            self.price_with_off = self.price

    def save(self, *args, **kwargs):
        self.set_price_with_off()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره ها"
