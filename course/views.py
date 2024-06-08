from django.shortcuts import render
from .models import Course
from jalali_date import date2jalali


# Create your views here.
def course(request):
    courses = Course.objects.all()
    for course in courses:
        course.jalali_date_starter = date2jalali(course.date_starter).strftime('%Y/%m/%d')
    return render(request, 'course/course.html', context={"courses": courses})
