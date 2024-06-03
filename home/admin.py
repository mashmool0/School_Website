from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from .models import Course


@admin.register(Course)
class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['course_name', 'price', "teacher", "date_starter", "course_type", 'get_created_jalali']

    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')



