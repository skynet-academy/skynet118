from django.shortcuts import render
from .forms import CommentForm
from .models import Course 
from django.shortcuts import render, get_object_or_404

# Create your views here.


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


    return render(request, template_name, { 'course':course,
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form
                                            })




