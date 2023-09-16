from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
type_choices = (
    ('admin', 'Admin'),
    ('college', 'College'), 
    ('college_coordinator', 'College_Coordinator'),
)
class Course(models.Model):
    name = models.CharField(max_length=255)
    abb= models.CharField(max_length=15)
    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=20, choices=type_choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Add any additional fields you need

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def get_by_natural_key(self):
        return self.email
    

class College(BaseUser):
    name = models.CharField(max_length=255)
    address = models.TextField()
    is_verified = models.BooleanField(default=False)
    affiliated_univ = models.CharField(max_length=255)
    univ_address = models.TextField()
    mail = models.EmailField()
    contact = models.CharField(max_length=20)
    abbrevation = models.CharField(max_length=10,null=True,blank=True)
    

    def __str__(self):
        if(self.abbrevation):
            return self.abbrevation
        return self.name
    
class CourseCoordinator(BaseUser):
    name = models.CharField(max_length=255)
    affiliated_college = models.ForeignKey(College, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)
    designation = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name

class College_Course(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.college.name + ' - ' + self.course.name
    
    
class Coordinator_Course(models.Model):
    coordinator = models.ForeignKey(CourseCoordinator, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.coordinator.name + ' - ' + self.course.name


    

