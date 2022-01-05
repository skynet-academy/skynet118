from django.db import models
# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    date_pub = models.DateTimeField("Date Published")
    price = models.FloatField(default=0)
    nro_lessons = models.IntegerField()
    nro_tests = models.IntegerField()
    description = models.CharField(max_length=500, default="Description")
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.course_name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Package(models.Model):
    course_package = models.ForeignKey(Course, on_delete=models.CASCADE, related_name= 'course_package', null=True)
    package_name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    nro_lessons = models.IntegerField()
    comment = models.CharField(max_length=500)
    time = models.IntegerField()
    
    def __str__(self):
        return self.package_name


class Comment(models.Model):
    comment = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    body = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)

