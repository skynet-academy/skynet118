from django.shortcuts import render
from .models import Student
# Create your views here.

def calendar(request, student):
    #schedule_student = Student.objects.get(id=student)
    context = {}
    return render(request, "student/schedule.html", context)



