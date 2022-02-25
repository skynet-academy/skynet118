from django.urls import path, include

from . import views

app_name = "payments"

urlpatterns = [
        path("checkout/<int:pk>/<str:name>/", views.checkout, name="checkout"),
        path("checkout-trial/<int:id>/", views.checkout_trial, name="checkout-trial"),
        path("success/<str:name>/<str:idpay>", views.payment_complete,  name="success"),
        path("cart/", views.cart,  name="cart"),
        ]
