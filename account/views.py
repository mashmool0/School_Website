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

    user, created = CustomUser.objects.get_or_create(phone_number=phone)
    otp_code = str(random.randint(1000, 9999))
    otp_token = str(random.getrandbits(48))
    expire = timezone.now() + timedelta(minutes=2)
    user.otp_code = otp_code
    user.otp_token = otp_token
    user.otp_expire_at = expire
    user.otp_attempts = 0
    user.save()

    # اینجا بجا SMS مثلاً لاگ می‌گیری:
    send_otp(phone_number=phone, otp=otp_code)
    print(f"OTP code for {phone} is {otp_code}")

    return JsonResponse({"success": True, "otp_token": otp_token, "msg": "کد تایید ارسال شد"})
