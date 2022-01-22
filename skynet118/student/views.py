from django.shortcuts import render

# Create your views here.

def calendar(request, name):
    context = {}
    return render(request, "student/schedule.html", context)



