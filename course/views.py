from django.shortcuts import render
from .models import Course


# Create your views here.
def course(request):
    courses = Course.objects.all()
    return render(request, 'course/course.html', context={"courses": courses})
