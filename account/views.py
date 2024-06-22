from urllib.parse import urlencode
from django.contrib import messages
from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from .models import WelcomeRegister, Otp, UserStudent
from .forms import RegisterForm, LoginForm, LoginOnlyWithPhone
from django.contrib.auth.models import User
from .decorators import un_authenticated, exist_otp, just_super_student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .send_otp_sms import send_otp
from django.utils.crypto import get_random_string
from .tasks import delete_expired_otp2, delete_expired_otp2_1, delete_expired_otp, delete_expired_otp_1
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from time import sleep


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
        phone_number = form.data.get("phone_number")  # Get phone number from POST data
        if phone_number.startswith("0"):
            phone_number = phone_number[1:]

        if User.objects.filter(username=phone_number).exists() and Otp.objects.filter(
                phone_number=phone_number).exists():
            # If user already exists, start the delete_expired_otp2_1 function
            delete_expired_otp2_1(phone_number)
            form.add_error(None, "لطفا یک دقیقه صبر کنید و دوباره تلاش کنید")

        elif form.is_valid():
            phone_number = form.cleaned_data.get("phone_number")
            if not User.objects.filter(username=phone_number).exists():
                try:
                    if not Otp.objects.filter(phone_number=phone_number).exists():
                        # save form with overwrite save method for check password and bug of in input
                        user_student, user = form.save()

                        # Add user to a Group in this method add it to Student user
                        Group.objects.get(name="Student").user_set.add(user)
                        token = get_random_string(99)
                        code, data = send_otp(phone_number)

                        # check otp send it was Successful or not
                        if data.get("Status") == "Success":
                            Otp.objects.create(phone_number=phone_number, token=token, code=code)
                            # run expired otp2 --> in this function if user don't log in will delete his account,
                            # otp message
                            delete_expired_otp2(phone_number)
                            request.session['otp_verified'] = True
                            return redirect(
                                reverse('account:authenticatePhone') + '?' + urlencode(
                                    {'token': token, 'phone': phone_number}))
                        else:
                            user.delete()
                            form.add_error(None,
                                           "در ارسال پیامک مشکلی ایجاد شده است لطفا با پشتیبانی سایت تماس بگیرید")
                            messages.error(request, 'Failed to send OTP. Please try again.')
                            return redirect('account:register')

                    else:
                        form.add_error(None, "لطفا یک دقیقه صبر کنید و دوباره تلاش کنید")
                        delete_expired_otp2_1(phone_number)
                except IntegrityError as e:
                    if 'phone_number' in str(e):
                        print("Integerity error")
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
                if Otp.objects.filter(phone_number=phone_number).exists():
                    form.add_error(None, "لطفا یک دقیقه صبر کنید و دوباره تلاش کنید")
                    delete_expired_otp2_1(phone_number)
                else:
                    form.add_error(None, 'این شماره قبلاً ثبت شده است')
        else:
            delete_expired_otp_1(phone_number)
    return render(request, 'account/Signup.html', context={'welcome_text': welcome_text, 'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home:home')


@un_authenticated
def user_login_with_phone(request):
    welcome_text = WelcomeRegister.objects.last()
    form = LoginOnlyWithPhone()
    if request.method == "POST":
        form = LoginOnlyWithPhone(request.POST)
        if form.is_valid():
            token_otp = get_random_string(length=99)
            phone_number = form.cleaned_data.get('phone_number')

            if not Otp.objects.filter(phone_number=phone_number).exists():
                if not User.objects.filter(username=phone_number).exists():
                    form.add_error(None, "این شماره قبلا ثبت نام نکرده است")
                else:
                    code, data = send_otp(phone_number)
                    # check status of send message
                    if data["Status"] == "Success":
                        Otp.objects.create(phone_number=phone_number, token=token_otp, code=code)
                        # delete this otp message after 5 minutes
                        delete_expired_otp(phone_number)
                        try:
                            # Changed: Redirect to the phone registration page with token as query parameter
                            return redirect(
                                reverse('account:phoneRegister') + '?' + urlencode(
                                    {'token': token_otp, 'phone': phone_number}))
                        except Exception as e:
                            Otp.objects.get(token=token_otp).delete()
                            form.add_error(None, "مشکلی در سایت به وجود آماده است ، بعدا دوباره تلاش کنید")
                            messages.error(request, f'خطایی رخ داده است: {str(e)}')
                            return redirect("home:home")
                    else:
                        delete_expired_otp_1(phone_number)
                        form.add_error(None, "مشکلی به وجود آمده لطفا دوباره تلاش کنید")
            else:
                form.add_error(None, "لطفا یک دقیقه صبر کنید و دوباره تلاش کنید")
                delete_expired_otp_1(phone_number)

        else:
            form.add_error(None, "شماره وارد شده ایراد دارد")

    # Render the login page if it's a GET request or if form is invalid
    return render(request, 'account/Login_with_phone.html', context={'welcome_text': welcome_text, "form": form})


@exist_otp
def user_phone_register(request):
    errors = []
    try:
        if request.POST:
            token_otp = request.GET.get('token')
            code = request.POST.get('1') + request.POST.get('2') + request.POST.get('3') + request.POST.get('4')
            phone_number = request.GET.get('phone')
            if Otp.objects.filter(token=token_otp, code=code).exists():
                if User.objects.filter(username=phone_number).exists():
                    login(request, User.objects.get(username=phone_number))
                    Otp.objects.filter(phone_number=phone_number).delete()
                    return redirect('home:home')
            else:
                return redirect("account:loginPhone")
        return render(request, 'account/ForgotPassword.html', context={"errors": errors})
    except Http404:
        raise Http404("Page not found")  # Catch Http404 exception explicitly

    except Exception as e:
        print("An error occurred:", str(e))
        if Otp.objects.filter(phone_number=request.GET.get('phone')).exists():
            Otp.objects.filter(phone_number=request.GET.get('phone').delete())
        raise


@exist_otp
def phone_register(request):
    errors = []
    try:
        request.session['otp_verified'] = True
        if request.POST:
            token_otp = request.GET.get('token')
            code = request.POST.get('1') + request.POST.get('2') + request.POST.get('3') + request.POST.get('4')
            phone_number = request.GET.get('phone')
            if Otp.objects.filter(token=token_otp, code=code).exists():
                login(request, User.objects.get(username=phone_number))
                Otp.objects.filter(phone_number=phone_number).delete()
                # todo redirect to fill information
                return redirect('home:home')
            else:
                return redirect("account:register")
        return render(request, 'account/phone_register.html', context={"errors": errors})
    except Http404:
        raise Http404("Page not found")  # Catch Http404 exception explicitly

    except Exception as e:
        print("An error occurred:", str(e))
        if Otp.objects.filter(phone_number=request.GET.get('phone')).exists():
            Otp.objects.filter(phone_number=request.GET.get('phone')).delete()
        raise


# if user exit from register phone function

@csrf_exempt
def handle_exit(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            phone_number = data.get('phone')

            # Ensure the phone number starts without zero
            if phone_number and phone_number.startswith("0"):
                phone_number = phone_number[1:]

            # Only delete the user if OTP verification is not completed
            if request.session.get('otp_verified', False):
                if User.objects.filter(username=phone_number).exists():
                    User.objects.get(username=phone_number).delete()

            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'failed', 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'failed', 'error': str(e)}, status=400)

    return JsonResponse({'status': 'failed', 'error': 'Invalid request method'}, status=400)
