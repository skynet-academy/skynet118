from .models import Comment, Course, Package 
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'date_pub', 'nro_lessons')

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'

