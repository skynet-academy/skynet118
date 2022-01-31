from django.shortcuts import render, redirect
from .forms import CommentForm, CourseForm, PackageForm
from django.http import HttpResponse
from .models import Course, Package
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from blog.decorators import allowed_users

# Create your views here.

def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request , 'courses/index_courses.html', context)


def course_package_view(request, fk):
    course = Course.objects.get(id=fk)
    package = Package.objects.all().filter(course_package=fk)
    context = {'package': package, 'course': course }
    return render(request, 'courses/course_package.html', context)


@allowed_users(allowed_roles=['admin', 'teachers'])
def create_course(request):
    course = CourseForm()
    if(request.method == "POST"):
        course = CourseForm(request.POST, request.FILES)
        if(course.is_valid()):
            course.save()
    context = {'course': course}
    return render(request, 'courses/create_course.html', context)

def course_view(request, id):
    course = Course.objects.get(id=id)
    context = {
        "course": course
            }
    return render(request, 'courses/course_view.html', context) 

@allowed_users(allowed_roles=['admin', 'teachers'])
def update_course(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(instance=course)
    if(request.method == "POST"):
        form = CourseForm(request.POST, instance=course)
        if(form.is_valid()):
            form.save()
            return redirect("/courses/")
    context = {'form': form}
    return render(request, 'courses/update_course.html', context)


@allowed_users(allowed_roles=['admin', 'teachers'])
def delete_course(request, pk):
    course = Course.objects.get(id=pk)
    if(request.method == "POST"):
        package.delete()
        return redirect("/courses/")

    context = {"item": course}
    return render(request, 'courses/delete_course.html', context)


def post_detail(request, slug):
    template_name = 'post_detail.html'
    course = get_object_or_404(Course, slug=slug)
    comments = course.comments.filter(active=True)
    new_comment = None
    
    if(request.method == 'POST'):
        comment_form = CommentForm(data=request.POST)
        if(comment_form.is_valid()):
                new_comment = comment_form.save(commit=False)
                new_comment.course = course 
                new_comment.save()
    else:
        comment_form = CommentForm()

    context = { 
            'course':course,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form
            }

    return render(request, template_name, context)


@allowed_users(allowed_roles=['admin', 'teachers'])
def create_package(request):
    form = PackageForm()
    if(request.method == "POST"):
        form = PackageForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/courses/')

    context = {'form': form}
    return render(request, 'courses/create_package.html', context)


@allowed_users(allowed_roles=['admin', 'teachers'])
def update_package(request, pk):
    package = Package.objects.get(id=pk)
    form = PackageForm(instance=package)
    if(request.method == "POST"):
        form = PackageForm(request.POST, instance=package)
        if(form.is_valid()):
            form.save()
            return redirect("/courses/")
    context = {'form': form}
    return render(request, 'courses/update_package.html', context)


@allowed_users(allowed_roles=['admin', 'teachers'])
def delete_package(request, pk):
    package = Package.objects.get(id=pk)
    if(request.method == "POST"):
        package.delete()
        return redirect("/courses/")

    context = {"item": package}
    return render(request, 'courses/delete.html', context)


