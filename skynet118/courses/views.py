from django.shortcuts import render, redirect
from .forms import CommentForm, CourseForm, PackageForm
from django.http import HttpResponse
from .models import Course, Package
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    courses = Course.objects.all()
    packages = Package.objects.all()
    if(request.method == "POST"):
        name = request.POST['name']
        context = "hello world"
        return HttpResponse(context)

    context = {'courses': courses, 'packages': packages}
    return render(request , 'courses/index_courses.html', context)


def create_course(request):
    form = CourseForm()
    if(request.method == "POST"):
        form = CourseForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/courses/')
    context = {'form': form}
    return render(request, 'courses/create_course.html', context)


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


def create_package(request):
    form = PackageForm()
    if(request.method == "POST"):
        form = PackageForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/courses/')

    context = {'form': form}
    return render(request, 'courses/create_package.html', context)


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

def delete_package(request, pk):
    package = Package.objects.get(id=pk)
    if(request.method == "POST"):
        package.delete()
        return redirect("/courses/")

    context = {"item": package}
    return render(request, 'courses/delete.html', context)


