from django.shortcuts import render
from .models import Course
from jalali_date import date2jalali
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def course(request):
    courses = Course.objects.all()
    for course in courses:
        course.jalali_date_starter = date2jalali(course.date_starter).strftime('%Y/%m/%d')
    return render(request, 'course/course.html', context={"courses": courses})


@csrf_exempt  # Temporarily disable CSRF protection for simplicity
def add_to_basket(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        # Logic to update the model
        try:
            course_user = Course.objects.get(id=course_id)
            # Update the model as needed, for example, add the course to a user's basket
            # user.basket.add(course)  # Assuming you have a basket field in your user model
            response = {'status': 'success', 'message': 'Course added to basket'}
        except Course.DoesNotExist:
            response = {'status': 'error', 'message': 'Course not found'}
    else:
        response = {'status': 'error', 'message': 'Invalid request'}

    return JsonResponse(response)
