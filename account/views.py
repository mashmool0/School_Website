# account/views.py

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from .models import CustomUser
import random
from datetime import timedelta
from .send_otp_sms import send_otp
from django.views.decorators.csrf import csrf_exempt


def signup_step1_view(request):
    return render(request, "account/signup_step1.html")


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
    otp_token = str(random.getrandbits(48))
    expire = timezone.now() + timedelta(minutes=2)
    user.otp_code = otp_code
    user.otp_token = otp_token
    user.otp_expire_at = expire
    user.otp_attempts += 0
    user.save()
    print(f"OTP code for {phone} is {otp_code}")

    return JsonResponse({"success": True, "otp_token": otp_token, "msg": "کد تایید ارسال شد"})


def verify_otp_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "فقط متد POST مجاز است"}, status=405)

    import json
    try:
        data = json.loads(request.body)
        phone = data.get("phone_number")
        otp = data.get("otp")
        otp_token = data.get("otp_token")
    except Exception:
        return JsonResponse({"error": "درخواست نامعتبر."}, status=400)

    if not (phone and otp and otp_token):
        return JsonResponse({"error": "همه فیلدها الزامی است."}, status=400)

    try:
        user = CustomUser.objects.get(phone_number=phone, otp_token=otp_token)
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
    user.otp_token = ""
    user.otp_expire_at = None
    user.otp_attempts = 0
    user.is_active = True  # یا هر flag مناسب (اگر حساب باید فعال شود)
    user.save()

    # شما می‌توانید یک توکن یا flag ثبت‌نام مرحله بعدی هم به خروجی اضافه کنید
    return JsonResponse({"success": True, "msg": "تایید شد. لطفاً اطلاعات تکمیلی خود را وارد کنید."})


def signup_step2_view(request):
    return render(request, "account/signup_step2.html")
