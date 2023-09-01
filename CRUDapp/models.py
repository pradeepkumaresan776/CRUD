from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    name = models.CharField(max_length=20, default='')
    age = models.IntegerField(default='')
    mail = models.CharField(max_length=30, default='')
    gender = models.CharField(max_length=10, default='')
    phnumber = models.IntegerField(default='')