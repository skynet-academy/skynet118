from django.urls import path, include
from . import views

#include("blog")
app_name = 'blog'


urlpatterns = [
        path("", views.index.as_view(), name = "index"),
        path("profile/", views.profile , name = "profile"),
        path("contact/", views.ContactView.as_view(), name = "contact"),
        path("contact_create/", views.contact_create, name = "contact-create"),
        #path("contact/", views.ContactView.as_view(), name = "contact"),
        path("portfolio/", views.PortfolioView.as_view(), name = "portfolios"),
        path("portfolio_create/", views.portfolio_create, name = "portfolio-create"),
        path("portfolio/<slug:slug>", views.PortfolioDetailView.as_view(), name = "portfolio"),
        path("comment/", views.CommentView.as_view(), name = "comments"),
        path("comment/<slug:slug>", views.CommentDetailView.as_view(), name = "comment-detail"),
        ]














