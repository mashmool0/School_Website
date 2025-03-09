from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.password_validation import validate_password

from .models import Basket, UserPayment
from account.models import UserStudent
from course.models import Course
from .decorators import show_information, show_information_to_submit_user


# Create your views here.

@login_required(login_url="account:login")
def course_panel(request):
    return render(request, 'panel/bought_courses.html', context={})


@login_required(login_url="account:login")
def basket_panel(request):
    baskets = Basket.objects.filter(basket_user=request.user)
    total_sum = sum(item.price for item in baskets)
    return render(request, 'panel/basket.html', context={'baskets': baskets, 'total_sum': total_sum})


@login_required(login_url="account:login")
def last_order(request):
    return render(request, 'panel/latest_transitions.html', context={})


@show_information_to_submit_user
def show_user_info(request):
    if UserStudent.objects.filter(phone_number=request.user.username).exists():
        user_student = UserStudent.objects.filter(phone_number=request.user.username).last()
        user_student.user_birthday_date = str(user_student.birthday_date)
        return render(request, 'panel/show_info.html', context={"user_student": user_student})

    return render(request, 'panel/show_info.html', context={})


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
            user_student.father_serial_number = request.POST.get("DarsBabash")
            user_student.mother_serial_number = request.POST.get("DarsMommy")
            user_student.is_information_submited = True
            user_student.save()  # Save the changes to the database
            context = {
                "message": "اطلاعات با موفقیت ذخیره شد.برای دیدن اطلاعات شخصی خود صفحه را رفرش کنید .اگر با اطلاعات "
                           "ثبت شده مشکلی دارید برای ویرایش با مدرسه تماس "
                           " بگیرید "}
        except UserStudent.DoesNotExist:
            context = {"error": "کاربر یافت نشد."}

    else:
        context = {}

    return render(request, "panel/information.html", context)


@csrf_exempt  # Temporarily disable CSRF protection for simplicity
def add_to_basket(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            response = {"status": "error", "message": "لطفا اول در سایت ثبت نام کنید"}
            return JsonResponse(response)
        course_id = request.POST.get('course_id')
        try:
            course_user = Course.objects.get(id=course_id)
            if Basket.objects.filter(course_name=course_user.course_name, teacher=course_user.teacher,
                                     basket_user=request.user).exists():
                response = {'status': 'error', 'message': 'این دوره قبلا اضافه شده است'}
            else:
                basket = Basket.objects.create(course_name=course_user.course_name, teacher=course_user.teacher,
                                               price=course_user.price,
                                               basket_user=request.user,
                                               price_with_off=course_user.price_with_off)
                basket.save()
                response = {'status': 'success', 'message': 'دوره به سبد خرید اضافه شد'}
        except Course.DoesNotExist:
            response = {'status': 'error', 'message': 'دوره یافت نشد'}
    else:
        response = {'status': 'error', 'message': 'درخواست نامعتبر'}

    return JsonResponse(response)


@login_required(login_url="account:login")
def change_password(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        if phone.startswith("0"):
            phone = phone[1:]
        current_pass = request.POST.get('current_pass').strip()
        new_pass = request.POST.get('new_pass').strip()
        if len(new_pass) < 8:
            error = 'تعداد ارقام رمز جدید بسیار کم است ، لطفا رمز عبور دیگری انتخاب کنید '
            return render(request, 'panel/change_password.html', context={"error": error})
        user = authenticate(username=phone, password=current_pass)

        if user is not None and user == request.user:
            user.set_password(new_pass)
            user.save()
            update_session_auth_hash(request, user)
            message = "عملیات موفقیت آمیز بود"
            return render(request, 'panel/change_password.html', context={"message": message})
        else:
            error = 'رمز عبور اشتباه است'
            return render(request, 'panel/change_password.html', context={"error": error})

    return render(request, 'panel/change_password.html', context={})


@csrf_exempt
@login_required(login_url="account:login")
def delete_form_basket(request):
    if request.method == "POST":
        basket_id = request.POST.get('basket_id')

        try:
            basket_item = Basket.objects.filter(id=basket_id, basket_user=request.user)
            basket_item.delete()
            response = {"status": "success", "message": "آیتم با موفقیت حذف شد"}
        except Basket.DoesNotExist:
            response = {"status": "error", "message": "آیتم مورد نظر در سبد خرید یافت نشد"}

    else:
        response = {"status": "error", "message": "درخواست نامعتبر"}

    return JsonResponse(response)


def payment_view(request):
    baskets = Basket.objects.filter(basket_user=request.user)
    total_sum = sum(item.price for item in baskets)

    if request.method == "POST":
        # دریافت کد تخفیف اگر وجود داشته باشد
        discount_code = request.POST.get('codeTakhfif', '0')

        # بررسی اعتبار کد تخفیف (این قسمت نیاز به پیاده‌سازی کامل دارد)
        discount_amount = 0
        # اگر کد تخفیف معتبر باشد، مقدار تخفیف را محاسبه کنید

        # مبلغ نهایی پس از اعمال تخفیف
        final_amount = total_sum - discount_amount

        # بررسی اینکه آیا تصویر رسید آپلود شده است
        if 'receipt_image' in request.FILES:
            # ایجاد یک مورد جدید در مدل UserPayment
            payment = UserPayment(
                user=request.user,
                amount=final_amount,
                receipt_image=request.FILES['receipt_image'],
                status='pending'
            )
            payment.save()

            # پیام موفقیت‌آمیز به کاربر نشان داده شود
            messages.success(request, 'رسید پرداخت شما با موفقیت آپلود شد و در انتظار تایید است.')

            # پاک کردن سبد خرید پس از ثبت موفق پرداخت
            # این بخش اختیاری است و بستگی به منطق برنامه دارد
            # baskets.delete()

            # انتقال به صفحه وضعیت پرداخت یا داشبورد
            return redirect('panel:payment_status')
        else:
            # اگر تصویر آپلود نشده باشد، پیام خطا نشان داده شود
            messages.error(request, 'لطفاً تصویر رسید پرداخت خود را آپلود کنید.')

    # اگر درخواست از نوع GET باشد یا فرم POST ناموفق باشد
    return render(request, 'panel/payment.html', context={
        'baskets': baskets,
        'total_sum': total_sum
    })
