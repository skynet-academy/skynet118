from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    teacher = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")
    image_url = models.CharField(max_length=1000, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    course = models.ForeignKey(Course, max_length=200, null=True, blank=True, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.name



