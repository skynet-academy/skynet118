from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, "Freshman"),
        (SOPHOMORE, "Sophomore"),
        (JUNIOR, "Junior"),
        (SENIOR, "Senior"),
        (GRADUATE, "Graduate"),
            ]
    year_in_school = models.CharField(max_length=2, choices= YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN,)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    #name = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    #students = models.ManyToManyField(Student, through='Schedule')

    def __str__(self):
        return self.name


#class Schedule(models.Model):
#    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#    pupil = models.ForeignKey(Student, on_delete=models.CASCADE)
#    date_schedule = models.DateField()
#    schedule = models.JSONField(default=dict)
#        
#    class Meta:
#        unique_together = [['teacher','pupil']]
