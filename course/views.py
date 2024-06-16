from django.shortcuts import render
from .models import Course
from jalali_date import date2jalali
from account.models import Footer



def course_view(request):
    footer = Footer.objects.last()
    courses = Course.objects.all()
    for course in courses:
        course.jalali_date_starter = date2jalali(course.date_starter).strftime('%Y/%m/%d')
    return render(request, 'course/course.html', context={"courses": courses, 'footer': footer})


def filter_courses(request):
    footer = Footer.objects.last()
    course_type = request.GET.get('type')
    if course_type == 'all':
        courses = Course.objects.all()
    else:
        courses = Course.objects.filter(course_type=course_type)
    for course in courses:
        course.jalali_date_starter = date2jalali(course.date_starter).strftime('%Y/%m/%d')
    return render(request, 'course/course_cards.html', context={"courses": courses, 'footer': footer})
