from django.contrib import admin

# Register your models here.
from .models import BaseUser, CollegeSpoc, Course, CourseCoordinator
admin.site.register([BaseUser, CollegeSpoc, Course, CourseCoordinator])