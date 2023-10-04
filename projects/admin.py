from django.contrib import admin

# Register your models here.
from .models import ProjectEntry,Project_Technologies,Technologies,Student_Details,upvote,comment,comment_like,comment_reply
admin.site.register([ProjectEntry,Project_Technologies,Technologies,Student_Details,upvote,comment,comment_like,comment_reply])