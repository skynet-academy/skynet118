from django.urls import path, include

from . import views

app_name = "payments"

urlpatterns = [
        path("", views.payment_view, name="payments"),
        path("<int:pk>/payment-python/", views.payment_course, name="payment-course"),
        ]

