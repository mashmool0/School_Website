from django.contrib import admin
from .models import WelcomeRegister, UserStudent, Otp, ContactUs
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
from import_export.formats.base_formats import XLSX

admin.site.register(WelcomeRegister)
admin.site.register(Otp)
admin.site.register(ContactUs)


@admin.action(description='Export selected students to Excel')
def export_to_excel(modeladmin, request, queryset):
    resource = modeladmin.get_export_resource_class()
    dataset = resource().export(queryset)
    response = HttpResponse(dataset.xlsx,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="students.xlsx"'
    return response


@admin.register(UserStudent)
class UserStudentAdmin(ModelAdminJalaliMixin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'username', 'super_student_user')
    search_fields = ('phone_number', 'email', 'username')
    list_filter = ('super_student_user', 'grade', 'section', 'field_of_study')
    fieldsets = [
        ("اطلاعات کاربری", {"fields": [("phone_number", 'username', "email")]}),
        ("اطلاعات تکمیلی کاربر", {"fields": [('first_name', 'last_name'), ('birthday_date',
                                                                           'section'), ('grade', 'field_of_study'),
                                             ('student_code_id',
                                              'father_name'), ('mother_name', 'address'), ('father_phone',
                                                                                           'mother_phone'),
                                             ('father_job', 'mother_job'),
                                             ('father_education', 'mother_education'), ('job_father_address',
                                                                                        'job_mother_address'),
                                             ('father_serial_number', 'mother_serial_number'),
                                             ('sibling_education',)]}),
        ("دسترسی های کاربر", {"fields": ['super_student_user', 'user']}),
    ]
    readonly_fields = ('user',)
    actions = [export_to_excel]

    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')
