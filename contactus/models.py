from django.db import models
from account.models import UserStudent


# Create your models here.
class ContactUs(models.Model):
    phone_number = models.CharField(max_length=11, verbose_name="شماره تماس کاربر")
    name = models.CharField(max_length=30, verbose_name="نام کاربر")
    extra_information = models.CharField(max_length=50, null=True, blank=True, verbose_name='اطلاعات بیشتر از کاربر')
    subject = models.CharField(max_length=100, verbose_name="موضوع")
    text = models.TextField(verbose_name="متن")
    user_student_connect = models.ForeignKey(UserStudent, on_delete=models.SET_NULL, related_name="connector_to_us",
                                             blank=True, null=True)

    class Meta:
        verbose_name = "ارتباط کاربر ها با مدیرمدرسه"
        verbose_name_plural = "ارتباط کاربر ها با مدیرمدرسه"

    def __str__(self):
        return self.name + "--" + self.phone_number
