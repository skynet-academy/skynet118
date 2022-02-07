from django.shortcuts import render
from .models import Student, Schedule, Teacher
from django.db.models import Q
# Create your views here.


def my_courses(request, usr):
    schedule = Schedule.objects.all()
    context = {'schedule': schedule}
    return render(request, "student/courses.html", context)


def calendar(request, student):
    schedule_student = Student.objects.get(id=student)
    context = {}
    return render(request, "student/schedule.html", context)
