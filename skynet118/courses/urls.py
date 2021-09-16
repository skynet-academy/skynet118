from django.urls import path, include


from . import views

#include("blog")
app_name = 'courses'


urlpatterns = [
        path("", views.index, name = "index"),
        #path("course/", views.payment(), name = "payment"),
        path("<slug:slug>/", views.post_detail, name = "post_detail"),
        ]














