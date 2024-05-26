from django.contrib import admin
from .models import WelcomeRegister, UserStudent

# Register your models here.
admin.site.register(WelcomeRegister)


@admin.register(UserStudent)
class UserStudentAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'first_name', 'super_student_user')
    search_fields = ('phone_number', 'email','username')
    list_filter = ('super_student_user',)
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
        ("دسترسی های کاربر", {"fields": ['super_student_user']}),
    ]
