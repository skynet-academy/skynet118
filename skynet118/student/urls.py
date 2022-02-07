from django.urls import path, include
from . import views

#include("blog")
app_name = 'student'


urlpatterns = [
        path("calendar/<str:student>", views.calendar, name = "calendar"),
        path("my-courses/<str:usr>", views.my_courses, name = "my-courses"),
        ]





