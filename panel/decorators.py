from django.shortcuts import redirect
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError


def show_information(view_func):
    def wrapper_func(request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                if request.user.user_student.is_information_submited:
                    return redirect("panel:basket")  # todo change it to user
                else:
                    return view_func(request, *args, **kwargs)
            else:
                return redirect("account:login")
        except Http404:
            # Handle Http404 exceptions (Page Not Found)
            return HttpResponseNotFound('<h1>Page not found</h1>')

    return wrapper_func
