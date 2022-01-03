from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField 
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class UserProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Portfolio(models.Model):
    
    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]
     
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    skills = models.JSONField(default=dict)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.user}" 
   
    def save(self, *args, **kwargs):
        super(Portfolio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Comment(models.Model):
    
    class Meta:
        verbose_name_plural = 'Comment Profiles'
        verbose_name = 'Comment'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = models.SlugField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if(not self.id):
            self.slug = slugify(self.name)
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/comment/{self.slug}"
