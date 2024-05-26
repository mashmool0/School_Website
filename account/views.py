from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from .models import WelcomeRegister


# Create your views here.
def user_login(request):
    welcome_text = WelcomeRegister.objects.last()
    return render(request, 'account/Login.html', context={'welcome_text': welcome_text})


def user_register(request):
    welcome_text = WelcomeRegister.objects.last()
    return render(request, 'account/Signup.html', context={'welcome_text':welcome_text})


def user_logout(request):
    logout(request)
    return redirect('home:home')
