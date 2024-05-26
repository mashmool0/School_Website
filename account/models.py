from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class WelcomeRegister(models.Model):
    text = models.TextField(verbose_name="متن خوش آمد گویی صفحه ثبت نام")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "متن صفحه ثبت نام"
        verbose_name_plural = "متن صفحه ثبت نام "


class UserStudent(models.Model):
    # ٍrequired field for Register
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="شماره تلفن ثبت نام")
    email = models.EmailField(unique=True, verbose_name="آدرس ایمیل")
    password1 = models.CharField(max_length=100, verbose_name="رمز ورود")
    # required field for authenticate school
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="نام")
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="نام خانوادگی")
    birthday_date = models.DateField(verbose_name="تاریخ تولد")
    section = models.CharField(max_length=30, null=True, blank=True, verbose_name="مقطع تحصیلی")
    grade = models.CharField(max_length=30, null=True, blank=True, verbose_name="")
    field_of_study = models.CharField(max_length=30, null=True, blank=True, verbose_name="رشته تحصیلی")
    father_name = models.CharField(max_length=40, null=True, blank=True, verbose_name="نام پدر")
    mother_name = models.CharField(max_length=40, null=True, blank=True, verbose_name="نام و نام خانوادگی مادر")
    address = models.TextField(null=True, blank=True, verbose_name="آدرس منزل")
    father_phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="شماره تلفن پدر")
    mother_phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="شماره مادر")
    father_job = models.CharField(max_length=40, null=True, blank=True, verbose_name="شغل پدر")
    mother_job = models.CharField(max_length=40, null=True, blank=True, verbose_name="شغل مادر")
    father_education = models.CharField(max_length=50, null=True, blank=True, verbose_name="تحصیلات پدر")
    mother_education = models.CharField(max_length=50, null=True, blank=True, verbose_name="تحصیلات مادر")
    job_father_address = models.TextField(null=True, blank=True, verbose_name="آدرس شغل پدر")
    job_mother_address = models.TextField(null=True, blank=True, verbose_name="آدرس شغل مادر")
    student_code_id = models.CharField(max_length=10, null=True, blank=True, verbose_name="کد ملی دانش آموز")
    father_serial_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="شماره شناسنامه پدر")
    mother_serial_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="شماره شناسنامه مادر")
    # not required
    sibling_education = models.TextField(null=True, blank=True, verbose_name="تحصیلات خواهر یا برادر")
    profile = models.ImageField(default='static_files/profile/22_Profile.jpg', upload_to='media',
                                verbose_name="پروفایل")

    # last authenticate
    super_student_user = models.BooleanField(default=False, verbose_name="قابلیت پرداخت و ثبت نام")
    # Connect this Model to User Model with OneToOne Connection
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE, related_name="user_student")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "دانش آموز مورد نظر"
        verbose_name_plural = "اطلاعات کاربری دانش آموزان"
