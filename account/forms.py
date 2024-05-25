import re

from django import forms
from django.contrib.auth.password_validation import validate_password

from .models import UserStudent
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'password', 'type': 'password', 'dir': 'rtl', 'placeholder': 'رمز ورود'}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'password', 'type': 'password', 'dir': 'rtl', 'placeholder': 'تکرار رمز ورود'}))

    class Meta:
        model = UserStudent
        fields = ('phone_number', 'username')
        widgets = {
            'phone_number': forms.TextInput(
                attrs={'id': 'PhoneNumber', 'type': 'tel', 'dir': 'rtl', 'placeholder': 'شماره تلفن'}),
            'username': forms.TextInput(
                attrs={'id': 'PhoneNumber', 'type': 'tel', 'dir': 'rtl', 'placeholder': 'نام کاربری'})
        }

    def save(self, commit=True):
        user_student = super().save(commit=False)
        user = User.objects.create_user(
            username=self.cleaned_data.get('phone_number'),
            password=self.cleaned_data.get('password1'),
        )
        user_student.user = user

        if commit:
            user.save()
            user_student.save()

        return user_student

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Check if both passwords are provided and not empty
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("رمز عبور و تکرار آن با یکدیگر مطابقت ندارند")
            validate_password(password1)
        elif password1 or password2:
            raise forms.ValidationError("لطفاً هر دو فیلد رمز عبور را پر کنید")

        return cleaned_data




class LoginForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'password', 'type': 'password', 'dir': 'rtl', 'placeholder': 'رمز ورود'}))
    email_or_phone = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'email_or_phone', 'type': 'text', 'dir': 'rtl', 'placeholder': 'شماره تماس یا ایمیل'}))

    def clean_email_or_phone(self):
        data = self.cleaned_data['email_or_phone']
        if not re.match(r'^[(09)(9)][0-9]+$', data):
            raise forms.ValidationError("شماره موبایل با 09 یا 9 آغاز میشود")
        elif not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', data):
            raise forms.ValidationError('ایمیل به شکل غلطی وارد شده است')
        return data
