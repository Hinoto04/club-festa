from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import IntegerChoices
from django.contrib.auth.models import User as djangoUser

class User(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    year = models.IntegerField(default=2021)
    number = models.IntegerField()
    regi_date = models.DateField()
    django_user = models.ForeignKey(djangoUser, on_delete=CASCADE)
    email = models.EmailField()
    profile_message = models.CharField(max_length=200, default=' ')
    interested_in = models.CharField(max_length=20, default=' ')
    description = models.TextField(default=' ')
    lastedit = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.number) + self.name