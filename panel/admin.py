# from django.contrib import admin
# from .models import UserTransactions, UserCourse, Basket, UserPayment

# # Register your models here.

# admin.site.register(UserTransactions)
# admin.site.register(UserCourse)
# admin.site.register(UserPayment)


# @admin.register(Basket)
# class BasketAdmin(admin.ModelAdmin):
#     list_display = ['course_name', "teacher", "basket_user", 'price', "price_with_off"]
#     search_fields = ['basket_user__user_student__phone_number', 'basket_user__user_student__first_name',
#                      'basket_user__user_student__last_name', 'basket_user__user_student__student_code_id']

#     list_filter = ('course_name', "teacher")
