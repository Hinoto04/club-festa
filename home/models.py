from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import IntegerChoices
from django.contrib.auth.models import User as djangoUser

class User(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    year = models.IntegerField(default=2021)
    number = models.IntegerField()
    regi_date = models.DateField(auto_created=True)
    django_user = models.ForeignKey(djangoUser, on_delete=CASCADE)
    email = models.EmailField()
    profile_message = models.CharField(max_length=200, default=' ')
    interested_in = models.CharField(max_length=20, default=' ')
    description = models.TextField(default=' ')
    lastedit = models.DateField(auto_now=True, auto_now_add=False)
    like = models.TextField(default='/')
    noticelike = models.TextField(default='/')

    def __str__(self):
        if self.type == 'Student':
            return str(self.number) + " " + self.name
        else:
            return self.name