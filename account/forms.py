import re

from django import forms
from django.contrib.auth.password_validation import validate_password

from .models import UserStudent
from django.contrib.auth.models import User

from django import forms
from .models import UserStudent


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"dir": "rtl", 'placeholder': 'رمز ورود'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"dir": "rtl", 'placeholder': 'تکرار رمز ورود'}))

    class Meta:
        model = UserStudent
        fields = ('phone_number', 'username', 'password1', 'password2')
        widgets = {
            'phone_number': forms.TextInput(attrs={"dir": "rtl", 'maxlength': '11', 'placeholder': 'شماره تلفن'}),
            'username': forms.TextInput(attrs={"dir": "rtl", 'placeholder': 'نام کاربری'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("رمز عبور و تکرار آن با یکدیگر مطابقت ندارند")
        if password1:
            try:
                validate_password(password1)
            except forms.ValidationError as error:
                self.add_error('password1', error)

        return cleaned_data


    def save(self, commit=True):



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
