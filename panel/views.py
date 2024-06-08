from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from account.models import UserStudent
from course.models import Course
from .decorators import show_information


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
@show_information
def user_info(request):
    if request.method == "POST" and UserStudent.objects.filter(phone_number=request.user.username).exists():
        try:
            user_student = UserStudent.objects.get(phone_number=request.user.username)
            user_student.first_name = request.POST.get("name")
            user_student.last_name = request.POST.get("lastName")
            user_student.birthday_date = request.POST.get("BD")
            user_student.grade = request.POST.get("paye")
            user_student.section = request.POST.get("grade")
            user_student.field_of_study = request.POST.get("reshte")
            user_student.student_code_id = request.POST.get("IDCode")
            user_student.mother_name = request.POST.get("mamanesh")
            user_student.father_name = request.POST.get("babash")
            user_student.address = request.POST.get("Khoone")
            user_student.father_phone = request.POST.get("babashPhone")
            user_student.mother_phone = request.POST.get("mamaneshPhone")
            user_student.father_job = request.POST.get("KarBabash")  # todo
            user_student.mother_job = request.POST.get("KarMommy")
            user_student.mother_education = request.POST.get("TahsilMommy")
            user_student.father_education = request.POST.get("TahsilBabash")
            user_student.job_mother_address = request.POST.get("AddressBabash")
            user_student.job_father_address = request.POST.get("AddressMommy")
            user_student.sibling_education = request.POST.get("DarsKharBeraresh")
            user_student.is_information_submited = True
            user_student.save()  # Save the changes to the database
            context = {
                "message": "اطلاعات با موفقیت ذخیره شد.اگر با اطلاعات ثبت شده مشکلی دارید برای ویرایش با مدرسه تماس "
                           "بگیرید"}
        except UserStudent.DoesNotExist:
            context = {"error": "کاربر یافت نشد."}

    else:
        context = {}

    return render(request, "panel/information.html", context)


@csrf_exempt  # Temporarily disable CSRF protection for simplicity
def add_to_basket(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
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
