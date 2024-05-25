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
    # Required fields for registration
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="شماره تلفن ثبت نام")
    email = models.EmailField(unique=True, verbose_name="آدرس ایمیل")
    # Required fields for authenticating school
    first_name = models.CharField(max_length=50, verbose_name="نام", blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی", blank=True, null=True)
    birthday_date = models.DateField(verbose_name="تاریخ تولد")
    section = models.CharField(max_length=30, verbose_name="مقطع تحصیلی", blank=True, null=True)
    grade = models.CharField(max_length=30, verbose_name="پایه تحصیلی", blank=True, null=True)  # Added descriptive name
    field_of_study = models.CharField(max_length=30, verbose_name="رشته تحصیلی", blank=True, null=True)
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
    # Not required
    sibling_education = models.TextField(verbose_name="تحصیلات خواهر یا برادر", blank=True, null=True)
    profile = models.ImageField(default='static_files/profile/22_Profile.jpg', upload_to='profiles/', verbose_name="پروفایل")
    # Last authenticate
    super_student_user = models.BooleanField(default=False, verbose_name="قابلیت پرداخت و ثبت نام")
    # Connect this Model to User Model with OneToOne Connection
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE, related_name="user_student")

    def __str__(self):
        full_name = f"{self.first_name or ''} {self.last_name or ''}".strip()
        return full_name if full_name else "Unnamed User"

    class Meta:
        verbose_name = "دانش آموز"
        verbose_name_plural = "اطلاعات کاربری دانش آموزان"
