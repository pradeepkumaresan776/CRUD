from django.contrib import admin
from .models import StudentDetails
# Register your models here.
class Student(admin.ModelAdmin):
    admin.site.register(StudentDetails)