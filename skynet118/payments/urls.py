from django.urls import path, include

from . import views

app_name = "payments"

urlpatterns = [
        path("checkout/<int:pk>/<str:name>/", views.checkout, name="checkout"),
        path("success/<str:name>/<str:idpay>", views.payment_complete,  name="success"),
        path("cart/", views.cart,  name="cart"),
        ]
