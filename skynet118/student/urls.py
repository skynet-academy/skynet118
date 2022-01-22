from django.urls import path, include
from . import views

#include("blog")
app_name = 'student'


urlpatterns = [
        path("calendar/<str:name>", views.calendar, name = "calendar"),
        ]





