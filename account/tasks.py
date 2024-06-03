# utils.py
import threading
import time
from .models import Otp
from django.shortcuts import redirect


def delete_expired_otp(otp_id):
    def delete_otp():
        time.sleep(300)  # Sleep for 5 minutes
        try:
            otp = Otp.objects.filter(token=otp_id)
            otp.delete()
            print(f"OTP with id {otp_id} has been deleted.")
            return redirect('account:loginPhone')
        except Otp.DoesNotExist:
            print(f"OTP with id {otp_id} does not exist.")

    thread = threading.Thread(target=delete_otp)
    thread.start()
