from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('withPhone/', views.user_login_with_phone, name='loginPhone'),
    path('phoneRegister/', views.user_phone_register, name='phoneRegister'),
    path('authenticatePhone/', views.phone_register, name='authenticatePhone'),
    path('contactus/', views.contact_us, name='contactUs'),
    path('logout/', views.user_logout, name='logout'),
]
