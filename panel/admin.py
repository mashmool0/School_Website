from django.contrib import admin
from .models import UserTransactions, UserCourse, Basket

# Register your models here.

admin.site.register(UserTransactions)
admin.site.register(UserCourse)


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['course_name', "teacher", "basket_user", 'price', "price_with_off"]
