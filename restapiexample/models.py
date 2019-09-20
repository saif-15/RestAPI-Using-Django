from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    age=models.IntegerField()
    department=models.CharField(max_length=20)
    

