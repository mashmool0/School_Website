from django.contrib import admin
from account.models import CustomUser, StudentProfile

admin.site.register(CustomUser)
admin.site.register(StudentProfile)
