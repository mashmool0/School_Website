# import re
# from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth.models import User
# from django import forms
# from .models import UserStudent
# from django.contrib.auth.hashers import make_password


# class RegisterForm(forms.ModelForm):
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={"dir": "rtl", 'placeholder': 'رمز ورود'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={"dir": "rtl", 'placeholder': 'تکرار رمز ورود'}))

#     class Meta:
#         model = UserStudent
#         fields = ('phone_number', 'username', 'password1', 'password2')
#         widgets = {
#             'phone_number': forms.TextInput(attrs={"dir": "rtl", 'maxlength': '11', 'placeholder': 'شماره تلفن'}),
#             'username': forms.TextInput(attrs={"dir": "rtl", 'placeholder': 'نام کاربری'}),
#         }

#     def clean_phone_number(self):
#         phone = self.cleaned_data.get('phone_number')
#         if not re.match(r'^(09|9)\d+$', phone):
#             raise forms.ValidationError("شماره موبایل با 09 یا 9 آغاز میشود")
#         if len(phone) < 10:
#             raise forms.ValidationError("شماره موبایل وارد شده صحیح نیست ")
#         if phone.startswith('0'):
#             phone = phone[1:]
#         return phone

#     def clean(self):
#         cleaned_data = super().clean()
#         password1 = cleaned_data.get('password1')
#         password2 = cleaned_data.get('password2')
#         if password1 and password2:
#             if password1 != password2:
#                 raise forms.ValidationError("رمز عبور و تکرار آن با یکدیگر مطابقت ندارند")
#         if password1:
#             try:
#                 validate_password(password1)
#             except forms.ValidationError as error:
#                 self.add_error('password1', error)

#         return cleaned_data

#     def save(self, commit=True):
#         user_student = super().save(commit=False)
#         password = self.cleaned_data.get('password1')
#         phone_number = self.cleaned_data.get('phone_number')

#         user = User.objects.create_user(username=phone_number, password=password)
#         user_student.set_user(user)

#         if commit:
#             user_student.save()
#         else:
#             User.delete(user)
#         return user_student, user


# class LoginForm(forms.ModelForm):
#     password1 = forms.CharField(widget=forms.PasswordInput(
#         attrs={'id': 'password', 'type': 'password', 'dir': 'rtl', 'placeholder': 'رمز ورود'}))
#     phone_number = forms.CharField(widget=forms.TextInput(
#         attrs={"maxlength": "11", 'dir': 'rtl', 'placeholder': 'شماره تماس'}))

#     class Meta:
#         model = User
#         fields = ('phone_number', 'password1')

#     def clean_phone_number(self):
#         data = self.cleaned_data['phone_number']
#         if not re.match(r'^(09|9)\d+$', data):
#             raise forms.ValidationError("شماره موبایل با 09 یا 9 آغاز میشود")
#         if len(data) < 10:
#             raise forms.ValidationError("شماره موبایل وارد شده صحیح نیست ")
#         if data.startswith('0'):
#             data = data[1:]
#         return data


# class LoginOnlyWithPhone(forms.Form):
#     phone_number = forms.CharField(
#         widget=forms.TextInput(attrs={"maxlength": "11", 'dir': 'rtl', 'placeholder': 'شماره تماس'}))

#     def clean_phone_number(self):
#         phone_number = self.cleaned_data.get('phone_number')
#         if not re.match(r'^(09|9)\d+$', phone_number):
#             raise forms.ValidationError("شماره موبایل با 09 یا 9 آغاز میشود")
#         if len(phone_number) < 10:
#             raise forms.ValidationError("شماره موبایل وارد شده صحیح نیست ")
#         if phone_number.startswith('0'):
#             phone_number = phone_number[1:]
#         return phone_number
