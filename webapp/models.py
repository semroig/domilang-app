from django.db import models

# Create your models here.

class Register(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=12)
    interest = models.IntegerField()

class Teacher(models.Model):
    name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    level = models.IntegerField() 

class Student(models.Model):
    name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    level = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,  related_name="workload")



