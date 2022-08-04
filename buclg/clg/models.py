from turtle import position
from unicodedata import name
from django.db import models

# Create your models here.
class Attendance (models.Model):
    name = models.CharField(max_length=100)
    sem = models.CharField(max_length=10)
    branch = models.CharField(max_length=100) 
    position = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name