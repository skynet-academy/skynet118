from django.contrib import admin
from .models import Purchase, Order, OrderItem 

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Purchase)
