from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.template import loader

from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

def index(request):
    context = {}
    return render(request, 'blog/index.html', context)

def profile(request):
    context = {}
    return render(request, 'blog/profile.html', context)










