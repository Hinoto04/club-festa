from django.db import models
from django.db.models.deletion import SET_DEFAULT
from home.models import User

class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=20, default='기타')
    isofficial = models.BooleanField(default=False)
    member = models.IntegerField(default=1)
    member_detail = models.TextField(default='', null=True, blank=True)
    appli = models.TextField(default="", null=True, blank=True)
    create_date = models.DateTimeField(auto_created=True)
    year = models.IntegerField(default=2021)
    club_master = models.ForeignKey(User, on_delete=SET_DEFAULT, default='')
    club_teacher = models.CharField(max_length=20, default='')
    club_thumbnail = models.TextField(default='')
    
    def __str__(self):
        return self.name