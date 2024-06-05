from django.db import models
from django.contrib.auth.models import User


class WelcomeRegister(models.Model):
    text = models.TextField(verbose_name="متن خوش آمد گویی صفحه ثبت نام")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "متن صفحه ثبت نام"
        verbose_name_plural = "متن‌های صفحه ثبت نام"  # Corrected for plural


class UserStudent(models.Model):
    GRADE = [
        ('nohom', 'نهم'),
        ('dahom', 'دهم'),
        ('yazdahom', 'یازدهم'),
        ('davazdahom', 'دوازدهم'),
    ]
    SECTION = [
        ("dabirestan", "دبیرستان دوره دوم"),
        ("rahnamii", "دبیرستان دوره اول"),
        ("dabestan", "دبستان"),
    ]

    STUDY = [
        ("tajrobi", "تجربی"),
        ("riazi", "ریاضی و فیزیک"),
        ("ensani", "انسانی"),
        ("honarestan", "هنرستان"),
        ("noOne", "هیچکدام(پایه نهم هستم)"),
    ]
    # Required fields for registration
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="شماره تلفن ثبت نام")
    username = models.CharField(max_length=30, verbose_name="نام")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_student", verbose_name="ارتباط با")
    # Required fields for authenticating school
    password1 = models.CharField(max_length=30, null=True, blank=True)
    password2 = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(verbose_name="آدرس ایمیل")
    first_name = models.CharField(max_length=50, verbose_name="نام", blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی", blank=True, null=True)
    birthday_date = models.DateField(verbose_name="تاریخ تولد", blank=True, null=True)
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

    def __str__(self):
        full_name = f"{self.first_name or ''} {self.last_name or ''}".strip()
        return full_name if full_name else self.username

    def set_user(self, user):
        self.user = user

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
