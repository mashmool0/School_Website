from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.course_view, name="course"),
    path('filter/', views.filter_courses, name='filter_courses'),
]
