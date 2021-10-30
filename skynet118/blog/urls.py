from django.urls import path, include
from . import views

#include("blog")
app_name = 'blog'


urlpatterns = [
        path("", views.index, name = "index"),
        path("profile/", views.profile, name = "profile"),
        ]














