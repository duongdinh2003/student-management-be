from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
