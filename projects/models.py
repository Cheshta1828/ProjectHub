from django.db import models
from accounts.models import CollegeSpoc, Course, CourseCoordinator, BaseUser
import requests
import uuid


    
    
    
class Technologies(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Student_Details(models.Model):
    poc_name = models.CharField(max_length=255)
    poc_email = models.EmailField()
    team_members_details=models.CharField(max_length=1000)#json field-dict of dict
    college = models.ForeignKey(CollegeSpoc, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_coordinator = models.ForeignKey(CourseCoordinator, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

		
class ProjectEntry(models.Model):
    
    name_of_project = models.CharField(max_length=255)
    description_of_project = models.TextField()
    views=models.IntegerField(default=0) 
    
    thumbnail_of_project = models.ImageField(upload_to='thumbnails/')
    image1 = models.ImageField(upload_to='project_images/',blank=True)#if uploaded to be validated
    image2 = models.ImageField(upload_to='project_images/',blank=True)
    image3 = models.ImageField(upload_to='project_images/',blank=True)
    video = models.URLField(max_length=200, blank=True)
    link1 = models.URLField(max_length=200, blank=True)
    link2 = models.URLField(max_length=200, blank=True)
    link3 = models.URLField(max_length=200, blank=True)
    report=models.FileField(upload_to='reports/')
    no_of_upvotes=models.IntegerField(default=0)
    no_of_comments=models.IntegerField(default=0)
    
    
    
    plag_percentage=models.DecimalField(max_digits=5, decimal_places=2, default=0.00)#approve function
    is_approved=models.BooleanField(default=False) #approve function to be written -publish before
    plagiarized_to=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)#approve function
    def __str__(self):
        return self.name_of_project
    def check_video_url(self,video_id):
        checker_url = "https://www.youtube.com/oembed?url="
        video_url = checker_url + video_id

        request = requests.get(video_url)

        return request.status_code == 200
    def save(self, *args, **kwargs):
        if not self.check_video_url(self.video):
            return "Please enter a valid youtube video url"
        
        super(ProjectEntry, self).save(*args, **kwargs)

class upvote(models.Model):
    upvoted_by=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    upvoted_to=models.ForeignKey(ProjectEntry,on_delete=models.CASCADE)

class comment(models.Model):
    commented_by=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    commented_on=models.ForeignKey(ProjectEntry,on_delete=models.CASCADE)
    no_of_upvotes=models.IntegerField(default=0)
    
class comment_like(models.Model):
    liked_by=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    liked_on=models.ForeignKey(comment,on_delete=models.CASCADE)

class comment_reply(models.Model):
    replied_by=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    replied_on=models.ForeignKey(comment,on_delete=models.CASCADE)



    
class Project_Technologies(models.Model):
    project = models.ForeignKey(ProjectEntry, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technologies, on_delete=models.CASCADE)

    def __str__(self):
        return self.technology.name
class Project_Team_Members(models.Model):
    team_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(ProjectEntry, on_delete=models.CASCADE,null=True,blank=True)
    student = models.ForeignKey(Student_Details, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name
#upvote to and by to be written -top 

