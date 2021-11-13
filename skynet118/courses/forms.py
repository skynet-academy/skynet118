from .models import Comment, Course, Package 
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'

