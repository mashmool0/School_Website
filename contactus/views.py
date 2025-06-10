# from django.shortcuts import render
# from account.models import LimitContactUs
# from .models import ContactUs
# from django.contrib.auth.decorators import login_required
# from datetime import timedelta
# from django.utils import timezone
# import logging

# logger = logging.getLogger(__name__)


# # Create your views here.
# @login_required(login_url="home:home")
# def contact_us(request):
#     errors = []
#     message = []
#     if request.method == "POST":
#         try:
#             if LimitContactUs.objects.filter(phone_number=request.user.username).exists():
#                 limit_contact = LimitContactUs.objects.get(phone_number=request.user.username)
#                 if limit_contact and timezone.now() - limit_contact.date_set > timedelta(minutes=10):
#                     limit_contact.delete()
#                 else:
#                     errors.append("شما اخیرا پیام ارسال کرده اید تا ده دقیقه آینده اجازه ارسال پیام ندارید")
#             if request.user.user_student and not LimitContactUs.objects.filter(
#                     phone_number=request.user.username).exists():
#                 name = request.POST.get("name")
#                 subject = request.POST.get("subject")
#                 text = request.POST.get("message")
#                 phone_number = request.user.username
#                 connect = request.user.user_student
#                 ContactUs.objects.create(phone_number=phone_number, name=name, subject=subject, text=text,
#                                          user_student_connect=connect)
#                 LimitContactUs.objects.create(phone_number=phone_number)
#                 message.append("Successfully")

#             else:
#                 errors.append("شما اخیرا پیام ارسال کرده اید به مدت یک ساعت اجازه ارسال پیام ندارید")
#         except Exception as e:
#             print(e, "----moshekl")
#             errors.append("مشکلی پیش آمده لطفا دوباره تلاش کنید")
#             logger.error(f"Error in contact_us view: {e}")

#     if len(errors) > 2:
#         if errors[0] == errors[1]:
#             errors.pop(1)
#     return render(request, 'contactus/contactUs.html', context={"errors": errors, 'message': message})
