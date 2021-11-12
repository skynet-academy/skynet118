from django.urls import path, include

from . import views

app_name = "payments"

urlpatterns = [
        path(r"checkout/<int:pk>/<str:name>/", views.checkout, name="checkout"),
        path("complete/", views.payment_complete,  name="complete"),
        path("cart/", views.cart,  name="cart"),
        ]
