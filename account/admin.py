from django.contrib import admin
from .models import WelcomeRegister, UserStudent, Otp, Footer, SetPriceForSchool, PriceUserForSchool
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
from import_export.formats.base_formats import XLSX

admin.site.register(WelcomeRegister)
admin.site.register(Otp)
admin.site.register(Footer)
admin.site.register(SetPriceForSchool)


# Add this function for export user information
@admin.action(description='Export selected students to Excel')
def export_to_excel(modeladmin, request, queryset):
    resource = modeladmin.get_export_resource_class()
    dataset = resource().export(queryset)
    response = HttpResponse(dataset.xlsx,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="students.xlsx"'
    return response


@admin.register(PriceUserForSchool)
class PriceForSchoolAdmin(admin.ModelAdmin):
    search_fields = ('user_phone', 'user_name')

    fieldsets = [("اطلاعات کاربر", {"fields": [("user_name", "user_phone")]}),
                 ("اطلاعات راجب قیمت ها", {"fields": [("pardakht_shode", "baghimonde")]}),
                 ("اطلاعات چک ها", {"fields": [("price_check", "check_serial", "check_date"),
                                               ("price_check2", "check_serial2", "check_date2"),
                                               ("price_check3", "check_serial3", "check_date3")]})]


@admin.register(UserStudent)
class UserStudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'phone_number', 'first_name', 'last_name', 'username', 'super_student_user', 'is_information_submited')
    search_fields = ('phone_number', 'email', 'username', 'first_name', 'last_name', 'student_code_id')
    list_filter = ('super_student_user', 'grade', 'section', 'field_of_study', 'is_information_submited')
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
        ("دسترسی های کاربر", {"fields": ['super_student_user', 'user', "is_information_submited"]}),
    ]
    readonly_fields = ('user',)
    actions = [export_to_excel]
