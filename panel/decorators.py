from django.shortcuts import redirect
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError


def show_information(view_func):
    def wrapper_func(request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                if request.user.user_student.is_information_submited:
                    return redirect("panel:showInfo")
                else:
                    return view_func(request, *args, **kwargs)
            else:
                return redirect("account:login")
        except Http404:
            # Handle Http404 exceptions (Page Not Found)
            return HttpResponseNotFound('<h1>Page not found</h1>')

    return wrapper_func


def show_information_to_submit_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_student.is_information_submited:
                return view_func(request, *args, **kwargs)
            else:
                return redirect("panel:userInfo")

        else:
            return redirect("account:login")

    return wrapper_func
