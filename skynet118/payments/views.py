from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Courses
#from django.template import loader

from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.


def payment_view(request):
    return render(request, 'payments/index_payment.html', {})

def payment_view_dollars(request):
    return render(request, 'payments/index_payment_dollars.html', {})

#def payment_view(request):
#    courses = Courses.objects.order_by('-pub_date')[:5] 
#    context = {
#             "courses": courses
#             }
#
#    return render(request, "payments/index_payment.html", context)
#
#
#def payment_course(request):
#    pass
