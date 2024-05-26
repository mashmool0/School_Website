from django.shortcuts import redirect


def un_authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


