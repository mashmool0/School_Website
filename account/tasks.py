# utils.py
import threading
import time
from .models import Otp
from django.shortcuts import redirect
from django.contrib.auth.models import User


def delete_expired_otp(otp_id):
    def delete_otp():
        time.sleep(300)  # Sleep for 5 minutes
        try:
            otp = Otp.objects.filter(phone_number=otp_id)
            otp.delete()
            print(f"OTP with id {otp_id} has been deleted.")
            return redirect('account:loginPhone')
        except Otp.DoesNotExist:
            print(f"OTP with id {otp_id} does not exist.")

    thread = threading.Thread(target=delete_otp)
    thread.start()


def delete_expired_otp2(phone):
    print("hi")

    def delete_otp2():
        time.sleep(30)  # Sleep for 5 minutes
        try:
            otp = Otp.objects.filter(phone_number=phone)
            if otp.exists():
                User.delete(User.objects.get(username=phone))
                otp.delete()
                print(f"OTP with id {phone} has been deleted.")
                return redirect('account:loginPhone')
        except Otp.DoesNotExist:
            print(f"OTP with id {phone} does not exist.")

    thread = threading.Thread(target=delete_otp2)
    thread.start()
