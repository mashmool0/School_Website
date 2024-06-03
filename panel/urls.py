from django.urls import path
from . import views

app_name = 'panel'
urlpatterns = [
    path('course/', views.course_panel, name='course'),
    path('basket/', views.basket_panel, name='basket'),
    path('order/', views.last_order, name='lastOrder'),
]
