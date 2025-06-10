from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.utils import timezone
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number is required')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        max_length=11, unique=True, verbose_name="شماره تلفن ثبت نام")

    ROLE_CHOICES = [
        ('student', 'دانش‌آموز'),
        ('teacher', 'معلم'),
        ('admin', 'مدیر'),
    ]
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default='student')

    email = models.EmailField(verbose_name="آدرس ایمیل", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    # ------------ OTP داخلی ----------
    otp_code = models.CharField(
        max_length=6, blank=True, null=True, verbose_name="کدفعلی OTP")
    otp_token = models.CharField(
        max_length=100, blank=True, null=True, unique=True, verbose_name="توکن OTP")
    otp_expire_at = models.DateTimeField(
        blank=True, null=True, verbose_name="انقضای OTP")
    otp_attempts = models.PositiveSmallIntegerField(
        default=0, verbose_name="تعداد تلاش‌های OTP")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number

    def otp_is_valid(self):
        return self.otp_code and self.otp_expire_at and timezone.now() < self.otp_expire_at

    def reset_otp(self):
        self.otp_code = None
        self.otp_token = None
        self.otp_expire_at = None
        self.otp_attempts = 0
        self.save(update_fields=['otp_code', 'otp_token',
                  'otp_expire_at', 'otp_attempts'])

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"


class StudentProfile(models.Model):
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

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                related_name="student_profile", verbose_name="کاربر")

    username = models.CharField(max_length=30, verbose_name="نام کاربری")
    first_name = models.CharField(
        max_length=50, verbose_name="نام", blank=True, null=True)
    last_name = models.CharField(
        max_length=50, verbose_name="نام خانوادگی", blank=True, null=True)
    birthday_date = models.DateField(
        verbose_name="تاریخ تولد", blank=True, null=True)
    user_birthday_date = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="تاریخ تولد (رشته)")
    section = models.CharField(
        max_length=30, verbose_name="مقطع تحصیلی", blank=True, null=True, choices=SECTION)
    grade = models.CharField(
        max_length=30, verbose_name="پایه تحصیلی", blank=True, null=True, choices=GRADE)
    field_of_study = models.CharField(
        max_length=30, verbose_name="رشته تحصیلی", blank=True, null=True, choices=STUDY)
    father_name = models.CharField(
        max_length=40, verbose_name="نام پدر", blank=True, null=True)
    mother_name = models.CharField(
        max_length=40, verbose_name="نام و نام خانوادگی مادر", blank=True, null=True)
    address = models.TextField(verbose_name="آدرس منزل", blank=True, null=True)
    father_phone = models.CharField(
        max_length=11, verbose_name="شماره تلفن پدر", blank=True, null=True)
    mother_phone = models.CharField(
        max_length=11, verbose_name="شماره مادر", blank=True, null=True)
    father_job = models.CharField(
        max_length=40, verbose_name="شغل پدر", blank=True, null=True)
    mother_job = models.CharField(
        max_length=40, verbose_name="شغل مادر", blank=True, null=True)
    father_education = models.CharField(
        max_length=50, verbose_name="تحصیلات پدر", blank=True, null=True)
    mother_education = models.CharField(
        max_length=50, verbose_name="تحصیلات مادر", blank=True, null=True)
    job_father_address = models.TextField(
        verbose_name="آدرس شغل پدر", blank=True, null=True)
    job_mother_address = models.TextField(
        verbose_name="آدرس شغل مادر", blank=True, null=True)
    student_code_id = models.CharField(
        max_length=10, verbose_name="کد ملی دانش آموز", blank=True, null=True)
    father_serial_number = models.CharField(
        max_length=20, verbose_name="شماره شناسنامه پدر", blank=True, null=True)
    mother_serial_number = models.CharField(
        max_length=20, verbose_name="شماره شناسنامه مادر", blank=True, null=True)
    sibling_education = models.TextField(
        verbose_name="تحصیلات خواهر یا برادر", blank=True, null=True)
    user_profile = models.ImageField(
        verbose_name="پروفایل", blank=True, null=True)
    super_student_user = models.BooleanField(
        default=False, verbose_name="قابلیت پرداخت و ثبت نام")
    is_information_submited = models.BooleanField(
        default=False, verbose_name="کاربر اطلاعات شخصی خود را کامل کرده است")

    def __str__(self):
        full_name = f"{self.first_name or ''} {self.last_name or ''}".strip()
        return full_name if full_name else self.username

    class Meta:
        verbose_name = "دانش آموز"
        verbose_name_plural = "اطلاعات کاربری دانش آموزان"


class WelcomeRegister(models.Model):
    text = models.TextField(verbose_name="متن خوش آمد گویی صفحه ثبت نام")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "متن صفحه ثبت نام"
        verbose_name_plural = "متن‌های صفحه ثبت نام"


class LimitContactUs(models.Model):
    phone_number = models.CharField(max_length=11, verbose_name="شماره تماس")
    date_set = models.DateTimeField(auto_now_add=True)


class Footer(models.Model):
    boss_name = models.CharField(max_length=40, verbose_name="نام مدیر")
    phone_number = models.CharField(
        max_length=11, verbose_name="شماره تلفن مدرسه ")
    school_address = models.TextField(verbose_name="آدرس مدرسه")
    roubica = models.URLField(
        max_length=200, verbose_name="لینک کانال یا راه ارتباطی روبیکا شما")
    instagram = models.URLField(
        max_length=200, verbose_name="لینک کانال یا راه ارتباطی اینستاگرام شما")
    soroosh = models.URLField(
        max_length=200, verbose_name="لینک کانال یا راه ارتباطی سروش شما")

    class Meta:
        verbose_name = "فوتر سایت"
        verbose_name_plural = "فوتر سایت"

    def __str__(self):
        return self.boss_name + "   ---   " + self.school_address


class SetPriceForSchool(models.Model):
    price_for_rahnamaee = models.PositiveIntegerField(
        verbose_name="شهریه مقطع راهنمایی",
        help_text="قیمت را به تومان و بدون علائم نگارشی وارد کنید "
    )
    price_for_dabirestan = models.PositiveIntegerField(
        verbose_name="شهریه مقطع دبیرستان",
        help_text="قیمت را به تومان و بدون علائم نگارشی وارد کنید "
    )

    def __str__(self):
        return f"rahnamaee ---> {self.price_for_rahnamaee}  and  dabirestan ---> {self.price_for_dabirestan}"

    class Meta:
        verbose_name = "تنظیم شهریه مدرسه"
        verbose_name_plural = "تنظیم شهریه مدرسه"


class PriceUserForSchool(models.Model):
    pardakht_shode = models.PositiveIntegerField(
        verbose_name="مبلغ پرداخت شده", blank=True, null=True)
    baghimonde = models.PositiveIntegerField(
        verbose_name="مبلغ باقی مانده", blank=True, null=True)
    user_name = models.CharField(
        max_length=100, verbose_name="نام و نام خانوادگی کاربر")
    user_phone = models.CharField(max_length=12, verbose_name="شماره کاربر")
    # check detail
    price_check = models.PositiveIntegerField(
        verbose_name="قیمت چک اول", blank=True, null=True)
    check_serial = models.CharField(
        max_length=20, verbose_name="شماره سریال چک", blank=True, null=True)
    check_date = models.CharField(
        max_length=20, verbose_name="تاریخ چک", help_text="مثل 1402/02/02", blank=True, null=True)
    price_check2 = models.PositiveIntegerField(
        verbose_name="قیمت چک دوم", blank=True, null=True)
    check_serial2 = models.CharField(
        max_length=20, verbose_name="شماره سریال چک دوم", blank=True, null=True)
    check_date2 = models.CharField(
        max_length=20, verbose_name="تاریخ چک", help_text="مثل 1402/02/02", blank=True, null=True)
    price_check3 = models.PositiveIntegerField(
        verbose_name="قیمت چک سوم", blank=True, null=True)
    check_serial3 = models.CharField(
        max_length=20, verbose_name="شماره سریال چک سوم", blank=True, null=True)
    check_date3 = models.CharField(
        max_length=20, verbose_name="تاریخ چک", help_text="مثل 1402/02/02", blank=True, null=True)

    class Meta:
        verbose_name = "چک های دانش آموزان"
        verbose_name_plural = "چک های دانش آموزان"
