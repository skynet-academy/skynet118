from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

#include("blog")
app_name = 'blog'


urlpatterns = [
        # 
        path("register/", views.registerPage, name = "register"),
        path("login/", views.loginPage, name = "login-page"),
        path("logout/", views.logoutUser, name = "logout"),
        path(
            "password_reset/", 
            auth_views.PasswordResetView.as_view(
                template_name="blog/password_reset_form.html",
                email_template_name="blog/password_reset_email.html",
                subject_template_name="blog/password_reset_subject.txt",
                success_url = reverse_lazy('blog:password_reset_done') 
                ), 
            name = "password_reset"),

        path(
            "password_reset/done/",
            auth_views.PasswordResetDoneView.as_view(
                template_name="blog/password_reset_done.html"
                ),
            name = "password_reset_done"),

        path(
            "reset/<uidb64>/<token>/",
            auth_views.PasswordResetConfirmView.as_view(
                template_name="blog/password_reset_confirm.html",
                success_url = reverse_lazy('blog:password_reset_complete') 
                ),
            name = "password_reset_confirm"),
        path(
            "password_reset_complete/", 
            auth_views.PasswordResetCompleteView.as_view(
                template_name="blog/password_reset_complete.html"
                ), 
            name = "password_reset_complete"),

        path("restricted/", views.restricted_view, name = "restricted"),

        path("", views.index, name = "index"),
        path("contact/", views.contact_view, name = "contact"),
        path("contacts/", views.contacts_view, name = "contacts"),
        path("contact_create/", views.contact_create, name = "contact-create"),

        path("profile_create/", views.profile_create, name = "profile-create"),
        path("profile/<int:id>", views.profile_view, name = "profile"),
        path("profile_update/<int:id>", views.profile_update, name = "profile-update"),

        path("portfolio_create/", views.portfolio_create, name = "portfolio-create"),
        path("portfolios/", views.portfolios_view, name = "portfolios"),
        path("portfolio/<int:id>", views.portfolio_view, name = "portfolio"),
        path("portfolio_update/<int:pk>", views.portfolio_update, name = "portfolio-update"),

        path("comment/", views.CommentView.as_view(), name = "comments"),
        path("comment/<slug:slug>", views.CommentDetailView.as_view(), name = "comment-detail"),
        ]


