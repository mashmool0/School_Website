from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jalali_date import datetime2jalali, date2jalali


# Create your views here.

@login_required(login_url="account:login")
def course_panel(request):
    return render(request, 'panel/bought_courses.html', context={})


@login_required(login_url="account:login")
def basket_panel(request):
    return render(request, 'panel/basket.html', context={})


@login_required(login_url="account:login")
def last_order(request):
    return render(request, 'panel/latest_transitions.html', context={})


@login_required(login_url="account:login")
def user_info(request):
    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d')
    return render(request, "panel/information.html", context={'jalali_join': jalali_join})
