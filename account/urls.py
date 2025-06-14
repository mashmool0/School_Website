from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path("signup/", views.signup_step1_view, name="signup_step1"),
    path("api/register/request-otp/", views.request_otp_view, name="request_otp"),
    path("api/register/verify-otp/", views.verify_otp_view, name="verify_otp"),
    path("signup/verify/", views.signup_step2_view, name="signup_step2"),
    path("api/register/complete-profile/",
         views.complete_profile_view, name="complete_profile"),
    path("signup/complete/", views.signup_step3_view, name="signup_complete"),
    path("signup/complete/done", views.done, name="done_signup"),

]
