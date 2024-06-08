from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.course, name="course"),
    path('add_to_basket', views.add_to_basket, name="add_to_basket"),
]
