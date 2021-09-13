from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from club.models import Club

class Event(models.Model):
    title = models.CharField(max_length=100)
    host = models.ForeignKey(Club, on_delete=CASCADE)
    content = models.TextField()