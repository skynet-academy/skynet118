from django import forms
from .models import (
        Skill,
        UserProfile,
        ContactProfile,
        Testimonial,
        Media,
        Portfolio,
        Comment,
        Certificate
        )


class SkillForm(forms.ModelForm):
    
    class Meta:
        model = Skill 
        fields = '__all__'

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'

class ContactProfileForm(forms.ModelForm):

    class Meta:
        model = ContactProfile 
        fields = '__all__'

class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial 
        fields = '__all__'

class MediaForm(forms.ModelForm):

    class Meta:
        model = Media 
        fields = '__all__'

class PortfoliForm(forms.ModelForm):

    class Meta:
        model = Portfolio 
        fields = '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment 
        fields = '__all__'

class CertificateForm(forms.ModelForm):

    class Meta:
        model = Certificate 
        fields = '__all__'

