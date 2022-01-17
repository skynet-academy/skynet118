from django.urls import path, include
from . import views

#include("blog")
app_name = 'blog'


urlpatterns = [
        # 
        path("register/", views.registerPage, name = "register"),
        path("login/", views.loginPage, name = "login-page"),
        path("logout/", views.logoutUser, name = "logout"),
        path("restricted/", views.restricted_view, name = "restricted"),

        path("", views.index, name = "index"),
        path("contact/", views.contact_view, name = "contact"),
        path("contacts/", views.contacts_view, name = "contacts"),
        path("contact_create/", views.contact_create, name = "contact-create"),

        path("profile_create/", views.profile_create, name = "profile-create"),
        path("profile/<int:id>", views.profile_view, name = "profile"),

        path("portfolio_create/", views.portfolio_create, name = "portfolio-create"),
        path("portfolios/", views.portfolios_view, name = "portfolios"),
        path("portfolio/<int:id>", views.portfolio_view, name = "portfolio"),
        path("portfolio_update/<int:pk>", views.portfolio_update, name = "portfolio-update"),

        path("comment/", views.CommentView.as_view(), name = "comments"),
        path("comment/<slug:slug>", views.CommentDetailView.as_view(), name = "comment-detail"),
        ]


