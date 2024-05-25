from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from .models import WelcomeRegister
from .forms import RegisterForm, LoginForm


# Create your views here.
def user_login(request):
    welcome_text = WelcomeRegister.objects.last()
    form = LoginForm()
    return render(request, 'account/Login.html', context={'welcome_text': welcome_text, 'form': form})


def user_register(request):
    welcome_text = WelcomeRegister.objects.last()
    form = RegisterForm()
    return render(request, 'account/Signup.html', context={'welcome_text': welcome_text, 'form': form})


def user_logout(request):
    logout(request)
    return redirect('home:home')
