from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from .models import WelcomeRegister
from .forms import RegisterForm, LoginForm, UserStudent
from django.contrib.auth.models import User
import sys


# Create your views here.
def user_login(request):
    welcome_text = WelcomeRegister.objects.last()
    form = LoginForm()
    return render(request, 'account/Login.html', context={'welcome_text': welcome_text, 'form': form})


def user_register(request):
    welcome_text = WelcomeRegister.objects.last()
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                password2 = form.cleaned_data.get('password2')
                phone_number = form.cleaned_data.get('phone_number')
                # Attempt to create a new user
                user = User.objects.create_user(username=phone_number, password=password)
                form.save()
                login(request, user)
                return redirect('home:home')

            except IntegrityError as e:
                if 'phone_number' in str(e):
                    form.add_error('phone_number', 'این شماره تلفن قبلاً ثبت شده است. لطفاً شماره دیگری انتخاب کنید.')
                else:
                    messages.error(request, f'خطایی رخ داده است: {str(e)}')
            except Exception as e:
                username = form.cleaned_data.get('username')
                if User.objects.filter(username=username).exists():
                    User.objects.filter(username=username).delete()

                messages.error(request, f'خطایی رخ داده است: {str(e)}')

    return render(request, 'account/Signup.html', context={'welcome_text': welcome_text, 'form': form})


def user_logout(request):
    logout(request)
    return redirect('home:home')
