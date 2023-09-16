from django.contrib import admin

# Register your models here.
from .models import BaseUser, College, Course, CourseCoordinator
admin.site.register([BaseUser, College, Course, CourseCoordinator])