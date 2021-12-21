from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from .models import Order, Course, Package
import json
#from django.template import loader

from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

def simple_checkout(request):
    return render(request, 'payments/simple_checkout.html')

def checkout(request, pk, name):
    customer = request.user 
    course = Course.objects.get(id=pk)
    package = Package.objects.filter(course_package=pk, package_name=name)[0]
    #package = Package.objects.filter(course_package=pk).filter(package_name=name).only()
    context = {'package': package, 'course': course, 'customer': customer}
    return render(request, 'payments/checkout.html', context)

def cart(request):
    if(request.user.is_authenticated):
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items  = []
    context = {'items': items}
    return render(request, 'payments/cart.html', context)

def payment_complete(request):
    body = json.loads(request.body)
    print('BODY', body)
    course = Course.objects.get(id=body['course_id'])
    Order.objects.create(course=course)
    return JsonResponse('Payment complete', safe=False)
