from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from .models import Course


@admin.register(Course)
class CourseAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):  # Changed FirstModelAdmin to CourseAdmin
    list_display = ['course_name', 'price', 'teacher', 'date_starter', 'course_type', 'get_created_jalali']
    readonly_fields = ('price_with_off',)

    @admin.display(description='تاریخ شروع دوره')
    def get_jalali_date_starter(self, obj):
        return date2jalali(obj.date_starter).strftime('%Y/%m/%d')

    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')
