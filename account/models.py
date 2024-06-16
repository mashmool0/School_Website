from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class WelcomeRegister(models.Model):
    text = models.TextField(verbose_name="متن خوش آمد گویی صفحه ثبت نام")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "متن صفحه ثبت نام"
        verbose_name_plural = "متن‌های صفحه ثبت نام"  # Corrected for plural


class UserStudent(models.Model):
    GRADE = [
        ('haftom', 'هفتم'),
        ('hashtom', 'هشتم'),
        ('nohom', 'نهم'),
        ('dahom', 'دهم'),
        ('yazdahom', 'یازدهم'),
        ('davazdahom', 'دوازدهم'),
    ]
    SECTION = [
        ("rahnamii", "متوسطه اول"),
        ("dabirestan", "متوسطه دوم"),
    ]

    STUDY = [
        ("riazi", "ریاضی"),
        ("tajrobi", "تجربی"),
        ("ensani", "انسانی"),
    ]
    # Required fields for registration
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="شماره تلفن ثبت نام")
    username = models.CharField(max_length=30, verbose_name="نام کاربری")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_student", verbose_name="ارتباط با",
                                blank=True, null=True)

    # Required fields for authenticating school
    password1 = models.CharField(max_length=30, null=True, blank=True)
    password2 = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(verbose_name="آدرس ایمیل", null=True, blank=True)
    first_name = models.CharField(max_length=50, verbose_name="نام", blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی", blank=True, null=True)
    birthday_date = models.DateField(verbose_name="تاریخ تولد", blank=True, null=True)
    user_birthday_date = models.CharField(max_length=20, blank=True,
                                          null=True)  # user cant see this its just for save birthday in string
    section = models.CharField(max_length=30, verbose_name="مقطع تحصیلی", blank=True, null=True, choices=SECTION)
    grade = models.CharField(max_length=30, verbose_name="پایه تحصیلی", blank=True, null=True,
                             choices=GRADE)  # Added descriptive name
    field_of_study = models.CharField(max_length=30, verbose_name="رشته تحصیلی", blank=True, null=True, choices=STUDY)
    father_name = models.CharField(max_length=40, verbose_name="نام پدر", blank=True, null=True)
    mother_name = models.CharField(max_length=40, verbose_name="نام و نام خانوادگی مادر", blank=True, null=True)
    address = models.TextField(verbose_name="آدرس منزل", blank=True, null=True)
    father_phone = models.CharField(max_length=11, verbose_name="شماره تلفن پدر", blank=True, null=True)
    mother_phone = models.CharField(max_length=11, verbose_name="شماره مادر", blank=True, null=True)
    father_job = models.CharField(max_length=40, verbose_name="شغل پدر", blank=True, null=True)
    mother_job = models.CharField(max_length=40, verbose_name="شغل مادر", blank=True, null=True)
    father_education = models.CharField(max_length=50, verbose_name="تحصیلات پدر", blank=True, null=True)
    mother_education = models.CharField(max_length=50, verbose_name="تحصیلات مادر", blank=True, null=True)
    job_father_address = models.TextField(verbose_name="آدرس شغل پدر", blank=True, null=True)
    job_mother_address = models.TextField(verbose_name="آدرس شغل مادر", blank=True, null=True)
    student_code_id = models.CharField(max_length=10, verbose_name="کد ملی دانش آموز", blank=True, null=True)
    father_serial_number = models.CharField(max_length=20, verbose_name="شماره شناسنامه پدر", blank=True, null=True)
    mother_serial_number = models.CharField(max_length=20, verbose_name="شماره شناسنامه مادر", blank=True, null=True)
    sibling_education = models.TextField(verbose_name="تحصیلات خواهر یا برادر", blank=True, null=True)
    user_profile = models.ImageField(verbose_name="پروفایل", blank=True, null=True)
    super_student_user = models.BooleanField(default=False, verbose_name="قابلیت پرداخت و ثبت نام")

    is_information_submited = models.BooleanField(default=False,
                                                  verbose_name="کاربر اطلاعات شخصی خود را کامل کرده است")

    def __str__(self):
        full_name = f"{self.first_name or ''} {self.last_name or ''}".strip()
        return full_name if full_name else self.username

    def set_user(self, user):
        self.user = user

    # def save(self, *args, **kwargs):
    #     if self.user and UserStudent.objects.filter(user=self.user).exists():
    #         raise ValidationError("Each user can only have one UserStudent associated with them.")
    #     super(UserStudent, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "دانش آموز"
        verbose_name_plural = "اطلاعات کاربری دانش آموزان"


class Otp(models.Model):
    token = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=11, primary_key=True)
    code = models.CharField(max_length=4)
    expiration_date = models.DateTimeField(auto_now_add=True)

    # request_count = models.IntegerField(default=0)  # New field to track the number of requests
    # last_request_time = models.DateTimeField(auto_now_add=True)  # New field to track the last request time

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "اعتبارسنجی کاربر"
        verbose_name_plural = "اعتبارسنجی کاربران"


class LimitContactUs(models.Model):
    phone_number = models.CharField(max_length=11, verbose_name="شماره تماس")
    date_set = models.DateTimeField(auto_now_add=True)


class Footer(models.Model):
    boss_name = models.CharField(max_length=40, verbose_name="نام مدیر")
    phone_number = models.CharField(max_length=11, verbose_name="شماره تلفن مدرسه ")
    school_address = models.TextField(verbose_name="آدرس مدرسه")
    roubica = models.URLField(max_length=200, verbose_name="لینک کانال یا راه ارتباطی روبیکا شما")
    instagram = models.URLField(max_length=200, verbose_name="لینک کانال یا راه ارتباطی اینستاگرام شما")
    soroosh = models.URLField(max_length=200, verbose_name="لینک کانال یا راه ارتباطی سروش شما")

    class Meta:
        verbose_name = "فوتر سایت"
        verbose_name_plural = "فوتر سایت"

    def __str__(self):
        return self.boss_name + "   ---   " + self.school_address


class SetPriceForSchool(models.Model):
    price_for_rahnamaee = models.PositiveIntegerField(verbose_name="شهریه مقطع راهنمایی",
                                                      help_text="قیمت را به تومان و بدون علائم نگارشی وارد کنید ")
    price_for_dabirestan = models.PositiveIntegerField(verbose_name="شهریه مقطع دبیرستان",
                                                       help_text="قیمت را به تومان و بدون علائم نگارشی وارد کنید ")

    def __str__(self):
        return f"rahnamaee ---> {self.price_for_rahnamaee}  and  dabirestan ---> {self.price_for_dabirestan}"

    class Meta:
        verbose_name = "تنظیم شهریه مدرسه"
        verbose_name_plural = "تنظیم شهریه مدرسه"


class PriceUserForSchool(models.Model):
    pardakht_shode = models.PositiveIntegerField(verbose_name="مبلغ پرداخت شده", blank=True, null=True)
    baghimonde = models.PositiveIntegerField(verbose_name="مبلغ باقی مانده", blank=True, null=True)
    user_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی کاربر")
    user_phone = models.CharField(max_length=12, verbose_name="شماره کاربر")
    # check detail
    # first check
    price_check = models.PositiveIntegerField(verbose_name=" قیمت چک اول", blank=True, null=True)
    check_serial = models.CharField(max_length=20, verbose_name="شماره سریال چک", blank=True, null=True)
    check_date = models.CharField(max_length=20, verbose_name="تاریخ چک", help_text="مثل 1402/02/02", blank=True,
                                  null=True)

    # second check
    price_check2 = models.PositiveIntegerField(verbose_name="قیمت چک دوم", blank=True, null=True)
    check_serial2 = models.CharField(max_length=20, verbose_name="شماره سریال چک دوم", blank=True, null=True)
    check_date2 = models.CharField(max_length=20, verbose_name="تاریخ چک", help_text="مثل 1402/02/02", blank=True,
                                   null=True)

    # third check
    price_check3 = models.PositiveIntegerField(verbose_name="قیمت چک سوم", blank=True, null=True)
    check_serial3 = models.CharField(max_length=20, verbose_name="شماره سریال چک سوم", blank=True, null=True)
    check_date3 = models.CharField(max_length=20, verbose_name="تاریخ چک", help_text="مثل 1402/02/02", blank=True,
                                   null=True)

    class Meta:
        verbose_name = "چک های دانش آموزان"
        verbose_name_plural = "چک های دانش اموزان"


class Storage(models.Model):
    my_file = models.FileField()
