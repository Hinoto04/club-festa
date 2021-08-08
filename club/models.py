from django.db import models
from django.db.models.deletion import SET_DEFAULT
from home.models import User

class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, default='기타')
    isofficial = models.BooleanField(default=False)
    member = models.IntegerField()
    member_detail = models.TextField(default='')
    create_date = models.DateTimeField()
    club_master = models.ForeignKey(User, on_delete=SET_DEFAULT, default='')
    club_teacher = models.CharField(max_length=20, default='')
    club_thumbnail = models.TextField(default='')
    
    def __str__(self):
        return self.name