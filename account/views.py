from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from .models import WelcomeRegister, Otp
from .forms import RegisterForm, LoginForm, UserStudent
from django.contrib.auth.models import User
from .decorators import un_authenticated
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .send_otp_sms import send_otp
import uuid
import random


# Create your views here.
@un_authenticated
def user_login(request):
    welcome_text = WelcomeRegister.objects.last()
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:home')
            else:
                form.add_error(None, "رمز ورود یا شماره تماس اشتباه میباشد")
    return render(request, 'account/Login.html', context={'welcome_text': welcome_text, 'form': form})


@un_authenticated
def user_register(request):
    welcome_text = WelcomeRegister.objects.last()
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # check user is exists ?  if exist in database show error to user
            phone_number = form.cleaned_data.get("phone_number")
            if not User.objects.filter(username=phone_number).exists():
                # Now create user and user student with overwrite save method and login user
                try:
                    user_student, user = form.save()
                    login(request, user)
                    return redirect('home:home')

                except IntegrityError as e:
                    if 'phone_number' in str(e):
                        form.add_error('phone_number',
                                       'این شماره تلفن قبلاً ثبت شده است. لطفاً شماره دیگری انتخاب کنید.')
                    else:
                        messages.error(request, f'خطایی رخ داده است: {str(e)}')
                except Exception as e:
                    username = form.cleaned_data.get('phone_number')
                    if User.objects.filter(username=username).exists():
                        User.objects.filter(username=username).delete()

                    messages.error(request, f'خطایی رخ داده است: {str(e)}')
            else:
                form.add_error(None, 'این شماره قبلا ثبت شده است')

    return render(request, 'account/Signup.html', context={'welcome_text': welcome_text, 'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home:home')


def user_login_with_phone(request):
    welcome_text = WelcomeRegister.objects.last()
    if request.method == "POST":
        token_otp = uuid.uuid4()
        phone_number = request.GET.get('phone_number')
        Otp.objects.create(phone_number=phone_number, token=token_otp, code=random.randint(1000, 9999))
        return redirect(reverse('account:phoneRegister' + f'?token={token_otp}'))
    return render(request, 'account/Login_with_phone.html', context={'welcome_text': welcome_text})
