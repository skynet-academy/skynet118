from django.urls import path, include
from . import views

#include("blog")
app_name = 'courses'


urlpatterns = [
        path("", views.index, name = "index"),
        path("detail/", views.detail_course, name = "detail"),
        path("create/", views.create_course, name = "create"),
        ]














