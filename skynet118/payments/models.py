from django.db import models

# Create your models here.


class Courses(models.Model):
    courses = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

    def __str__(self):
        return self.courses 
