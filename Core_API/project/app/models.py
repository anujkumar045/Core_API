from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Contact=models.CharField(max_length=10)
    City=models.CharField(max_length=48)