# from django.db import models
# from account.models import UserStudent
# from django.contrib.auth.models import User


# # Create your models here.
# class Basket(models.Model):
#     course_name = models.CharField(max_length=40, verbose_name="نام آیتم")
#     teacher = models.CharField(max_length=40, verbose_name="استاد")
#     price = models.IntegerField(verbose_name="قیمت")
#     basket_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ارتباط با")
#     price_with_off = models.IntegerField(null=True, blank=True, verbose_name="قیمت با تخفیف ")

#     # when user add to basket add this item

#     def set_basket_user(self, user):
#         self.basket_user = user

#     def __str__(self):
#         return self.course_name

#     class Meta:
#         verbose_name = "سبد خرید کاربر"
#         verbose_name_plural = "سبد خرید کاربران"


# class UserCourse(models.Model):
#     date_add = models.DateField(auto_now_add=True, verbose_name="روز خرید شده دوره")
#     course_name = models.CharField(max_length=30, verbose_name="نام دوره")
#     description = models.CharField(max_length=100, verbose_name="توضیحات")
#     baghimande = models.CharField(max_length=20, verbose_name="قیمت باقی مانده")
#     pardakhtshode = models.CharField(max_length=20, verbose_name="پرداخت شده")
#     course_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="خریدار دوره")

#     def set_course_user(self, user):
#         self.course_user = user

#     def __str__(self):
#         return self.course_name

#     class Meta:
#         verbose_name = "دوره های کاربر"
#         verbose_name_plural = "دوره های کاربران"


# class UserTransactions(models.Model):
#     STATUS_CHOICES = [
#         ('Full', 'تکمیل شده'),
#         ('Not Full', 'تکمیل نشده'),
#     ]

#     pay = models.CharField(max_length=20, verbose_name='پرداخت شده')
#     status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name="وضعیت پراخت")
#     baghimande = models.CharField(max_length=50, verbose_name="باقی مانده از دوره")
#     item_name = models.CharField(max_length=30, verbose_name="نام آیتم")
#     date_pay = models.DateField(auto_now_add=True)
#     transaction_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ارتباط با")

#     def __str__(self):
#         return self.item_name

#     def set_transaction_user(self, user):
#         self.transaction_user = user

#     class Meta:
#         verbose_name = "پرداخت های اخیر کاربر"
#         verbose_name_plural = "پرداخت های اخیر کاربران"


# class UserPayment(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'در انتظار تایید'),
#         ('approved', 'تایید شده'),
#         ('rejected', 'رد شده'),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
#     amount = models.IntegerField(verbose_name="مبلغ پرداخت")
#     receipt_image = models.ImageField(upload_to='receipts/', verbose_name="تصویر رسید")
#     payment_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="وضعیت")
#     admin_comment = models.TextField(blank=True, null=True, verbose_name="توضیحات ادمین")

#     def __str__(self):
#         return f"پرداخت {self.id} - {self.user.username}"

#     class Meta:
#         verbose_name = "پرداخت کاربر"
#         verbose_name_plural = "پرداخت‌های کاربران"
#         ordering = ['-payment_date']
