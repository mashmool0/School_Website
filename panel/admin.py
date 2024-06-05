from django.contrib import admin
from .models import UserTransactions, UserCourse, Basket

# Register your models here.
admin.site.register(Basket)
admin.site.register(UserTransactions)
admin.site.register(UserCourse)
