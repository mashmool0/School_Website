from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url="account:login")
def course_panel(request):
    return render(request, 'panel/bought_courses.html', context={})


@login_required(login_url="account:login")
def basket_panel(request):
    # print(request.user.user_student.super_student_user)
    return render(request, 'panel/basket.html', context={})


@login_required(login_url="account:login")
def last_order(request):
    return render(request, 'panel/latest_transitions.html', context={})
