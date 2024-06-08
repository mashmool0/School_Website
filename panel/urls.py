from django.urls import path
from . import views

app_name = 'panel'
urlpatterns = [
    path('course/', views.course_panel, name='course'),
    path('basket/', views.basket_panel, name='basket'),
    path('order/', views.last_order, name='lastOrder'),
    path('info/', views.user_info, name='userInfo'),
    path('add_to_basket/', views.add_to_basket, name="add_to_basket"),
]
