# account/views.py

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from .models import CustomUser
import random
from datetime import timedelta
from .send_otp_sms import send_otp
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from .models import CustomUser, StudentProfile
from django.db import transaction
from django.contrib.auth import login, logout
from .decorators import basic_info_should_complete, un_authenticated


@un_authenticated
def signup_step1_view(request):
    return render(request, "account/signup_step1.html")


@un_authenticated
def request_otp_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "فقط متد POST مجاز است"}, status=405)

    import json
    try:
        data = json.loads(request.body)
        phone = data.get("phone_number")
    except Exception:
        phone = None

    if not phone:
        return JsonResponse({"error": "شماره موبایل الزامی است."}, status=400)

    # اینجا بجا SMS مثلاً لاگ می‌گیری:
    otp_code, data = send_otp(phone_number=phone)
    user, created = CustomUser.objects.get_or_create(phone_number=phone)
    expire = timezone.now() + timedelta(minutes=2)
    user.otp_code = otp_code
    user.otp_expire_at = expire
    user.otp_attempts += 0
    user.save()
    print(f"OTP code for {phone} is {otp_code}")

    return JsonResponse({"success": True, "msg": "کد تایید ارسال شد"})


@un_authenticated
def verify_otp_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "فقط متد POST مجاز است"}, status=405)

    import json
    try:
        data = json.loads(request.body)
        phone = data.get("phone_number")
        otp = data.get("otp")
    except Exception:
        return JsonResponse({"error": "درخواست نامعتبر."}, status=400)

    if not (phone and otp):
        return JsonResponse({"error": "همه فیلدها الزامی است."}, status=400)

    try:
        user = CustomUser.objects.get(phone_number=phone)
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "کد تایید یا شماره درست نیست."}, status=404)

    # اعتبارسنجی تاریخ انقضا
    now = timezone.now()
    if user.otp_expire_at < now:
        return JsonResponse({"error": "کد تایید منقضی شده است. دوباره درخواست دهید."}, status=400)

    # تعداد دفعات اشتباه
    if user.otp_attempts >= 5:
        return JsonResponse({"error": "تلاش بیش از حد! لطفا کمی صبر کنید."}, status=400)

    if user.otp_code != otp:
        user.otp_attempts += 1
        user.save()
        return JsonResponse({"error": "کد تایید صحیح نیست."}, status=401)

    # موفقیت، OTP reset
    user.otp_code = ""
    user.otp_expire_at = None
    user.otp_attempts = 0
    user.is_active = True  # یا هر flag مناسب (اگر حساب باید فعال شود)
    user.save()
    login(request, user=user)

    # شما می‌توانید یک توکن یا flag ثبت‌نام مرحله بعدی هم به خروجی اضافه کنید
    return JsonResponse({"success": True, "msg": "تایید شد. لطفاً اطلاعات تکمیلی خود را وارد کنید."})


@un_authenticated
def signup_step2_view(request):
    return render(request, "account/signup_step2.html")


@login_required
@basic_info_should_complete
def complete_profile_view(request):
    import json
    if request.method != "POST":
        return JsonResponse({"error": "فقط متد POST مجاز است."}, status=405)
    try:
        data = json.loads(request.body)
    except Exception:
        return JsonResponse({"error": "دیتای ورودی نامعتبر است."}, status=400)

    user = request.user
    try:
        with transaction.atomic():
            profile, created = StudentProfile.objects.get_or_create(user=user)
            profile.full_name = data.get("full_name", "")
            profile.student_code_id = data.get("national_id", "")
            profile.birth_date = parse_date(data.get("birth_date")) or None
            profile.previous_school = data.get("previous_school", "")
            profile.last_year_gpa = data.get("last_year_gpa") or None
            profile.father_name = data.get("father_name", "")
            profile.father_job = data.get("father_job", "")
            profile.father_education = data.get("father_education", "")
            profile.mother_name = data.get("mother_name", "")
            profile.mother_job = data.get("mother_job", "")
            profile.mother_education = data.get("mother_education", "")
            profile.mother_phone = data.get("mother_mobile", "")
            profile.father_phone = data.get("father_mobile", "")
            profile.basic_info = True
            profile.save()
    except Exception as e:
        return JsonResponse({"error": f"خطا هنگام ذخیره پروفایل: {str(e)}"}, status=500)

    return JsonResponse({"success": True, "msg": "ثبت اطلاعات تکمیلی انجام شد."})


@login_required
@basic_info_should_complete
def signup_step3_view(request):
    return render(request, "account/signup_step3.html")
