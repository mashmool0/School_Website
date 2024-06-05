from django.shortcuts import redirect
from .models import Otp


def un_authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def exist_otp(view_func):
    def wrapper_func(request, *args, **kwargs):
        phone_number = request.GET.get('phone')
        token_otp = request.GET.get('token')
        if phone_number and token_otp and Otp.objects.filter(phone_number=phone_number, token=token_otp).exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('account:login')

    return wrapper_func


def just_super_student(view_func):
    def wrapper_func(reqeust, *args, **kwargs):
        if reqeust.user.user_student.super_student_user:
            return view_func(reqeust, *args, **kwargs)
        else:
            # todo
            # shoma be in safhe dstresi nadarid bayad az madrese ejaze vorood begirid
            return redirect("home:home")

    return wrapper_func


