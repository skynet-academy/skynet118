from django.urls import path, include
from . import views

#include("blog")
app_name = 'courses'


urlpatterns = [
        path("", views.index, name = "index"),
        path("create/", views.create_course, name = "create"),
        ]














