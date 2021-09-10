from django.urls import path, include

from . import views

app_name = "payments"

urlpatterns = [
        path("", views.store, name="store"),
        path("checkout/<int:pk>/", views.checkout, name="checkout"),
        path("complete/", views.payment_complete,  name="complete"),
        #path("rubles/", views.payment_view, name="payment_view"),
        #path("dollars/", views.payment_view_dollars, name="payment_view_dollars"),
        ]

