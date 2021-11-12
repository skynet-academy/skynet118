from django.urls import path, include
from . import views

#include("blog")
app_name = 'courses'


urlpatterns = [
        path("", views.index, name = "index_course"),
        path("create_course/", views.create_course, name = "create_course"),
        #path("delete/", views.create_course, name = "create"),
        path("create_package/", views.create_package, name = "create_package"),
        path("update_package/<str:pk>", views.update_package, name = "update_package"),
        path("delete_package/<str:pk>", views.delete_package, name = "delete_package"),
    ]














