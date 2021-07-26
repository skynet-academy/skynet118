from django.db import models

# Create your models here.


class Courses(models.Model):
    courses = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    teacher = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    pub_date = models.DateTimeField("Date Published")

    def __str__(self):
        return self.courses 
