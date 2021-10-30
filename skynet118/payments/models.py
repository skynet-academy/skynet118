from django.db import models
from blog.models import Customer
from courses.models import Course

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, max_length=200, null=True, blank=True, on_delete = models.CASCADE)
    course_name = models.ForeignKey(Course, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transanction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id)

    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



