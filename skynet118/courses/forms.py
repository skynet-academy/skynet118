from .models import Comment, Course
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'date_pub', 'nro_lessons')


