from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_lenght=200)
    surname = models.CharField(max_lenght=200)
    age = models.IntegerField(max_lenght=3)
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, "Freshman"),
        (SOPHOMORE, "Sophomore"),
        (JUNIOR, "Junior"),
        (SENIOR, "Senior"),
        (GRADUATE, "Graduate"),
            ]
    year_in_school = models.CharField(max_lenght=2, choices= YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN,)

    
