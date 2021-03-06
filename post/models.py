from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from club.models import Club
from home.models import User
class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publicDate = models.DateTimeField(default=datetime(2021, 9, 12, 0, 0, 0, 0), auto_created=True)
    hotDate = models.DateTimeField(default=datetime(2021, 9, 12, 0, 0, 0, 0), auto_created=True)
    author = models.ForeignKey(User, on_delete=CASCADE)
    views = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_created=True)
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    isprivate = models.BooleanField(default=True)
    isnotice = models.BooleanField(default=False)
    club = models.ForeignKey(Club, on_delete=CASCADE)
    author = models.ForeignKey(User, on_delete=CASCADE)
    views = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_created=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)
    notice = models.ForeignKey(Notice, on_delete=CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=CASCADE)
    create_date = models.DateTimeField(auto_created=True)
    
    def __str__(self):
        return self.content