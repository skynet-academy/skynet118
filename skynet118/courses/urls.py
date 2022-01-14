from django.urls import path, include
from . import views

#include("blog")
app_name = 'courses'


urlpatterns = [
        path("", views.index, name = "index_course"),
        path("course_packages/<int:fk>", views.course_package_view, name = "course_packages"),
        path("course/<int:id>", views.course_view, name="course_view"),
        path("create_course/", views.create_course, name = "create_course"),
        path("update_course/<int:pk>", views.update_course, name = "update_course"),
        path("delete_course/<int:pk>", views.delete_course, name = "delete_course"),
        #path("delete/", views.create_course, name = "create"),
        path("create_package/", views.create_package, name = "create_package"),
        path("update_package/<str:pk>", views.update_package, name = "update_package"),
        path("delete_package/<str:pk>", views.delete_package, name = "delete_package"),
    ]














