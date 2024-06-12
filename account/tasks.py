# utils.py
import threading
import time
from .models import Otp
from django.shortcuts import redirect
from django.contrib.auth.models import User


def delete_expired_otp(otp_id):
    def delete_otp():
        time.sleep(60)  # Sleep for 1 minutes
        try:
            otp = Otp.objects.filter(phone_number=otp_id)
            otp.delete()
            print(f"OTP with id {otp_id} has been deleted.")
            return redirect('account:loginPhone')
        except Otp.DoesNotExist:
            print(f"OTP with id {otp_id} does not exist.")

    thread = threading.Thread(target=delete_otp)
    thread.start()


def delete_expired_otp_1(otp_id):
    def delete_otp():
        time.sleep(60)  # Sleep for 1 minutes
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
    def delete_otp2():
        print("delete otp2 run")  # Sleep for 1 minutes
        time.sleep(60)
        try:
            if Otp.objects.filter(phone_number=phone).exists():
                otp = Otp.objects.filter(phone_number=phone)
                otp.delete()
                print(f"OTP with id {phone} has been deleted")
                User.delete(User.objects.get(username=phone))
                print(f"user with id {phone} has been deleted")

            return redirect('account:loginPhone')

        except Otp.DoesNotExist:
            print("field in otp deleted")
            print(f"OTP with id {phone} does not exist.")

    thread = threading.Thread(target=delete_otp2)
    thread.start()


def delete_expired_otp2_1(phone):
    def delete_otp2_1():
        print("delete otp2 run")  # Sleep for 1 minutes
        time.sleep(360)
        try:
            if Otp.objects.filter(phone_number=phone).exists():
                otp = Otp.objects.filter(phone_number=phone)
                otp.delete()
                User.delete(User.objects.get(username=phone))
                print(f"OTP with id {phone} has been deleted")
                return redirect('account:loginPhone')

        except Otp.DoesNotExist:
            print("field in otp deleted")
            print(f"OTP with id {phone} does not exist.")

    thread = threading.Thread(target=delete_otp2_1)
    thread.start()
