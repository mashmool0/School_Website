from django.shortcuts import redirect
# from .models import Otp


def un_authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def basic_info_should_complete(view_func):
    def wrapper_func(request, *args, **kwargs):
        try:
            if request.user.student_profile.basic_info:
                return redirect("home:home")
            else:
                return view_func(request, *args, **kwargs)
        except:
            return view_func(request, *args, **kwargs)
    return wrapper_func
