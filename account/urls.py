from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path("signup/", views.signup_step1_view, name="signup_step1"),
    path("api/register/request-otp/", views.request_otp_view, name="request_otp"),
]
