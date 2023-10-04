from django.contrib import admin

# Register your models here.
from .models import BaseUser, CollegeSpoc, Course, CourseCoordinator,Visitor
admin.site.register([BaseUser, CollegeSpoc, Course, CourseCoordinator,Visitor])