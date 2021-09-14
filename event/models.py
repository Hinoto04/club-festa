from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from club.models import Club

class Event(models.Model):
    title = models.CharField(default='', max_length=100)
    host = models.ForeignKey(Club, on_delete=CASCADE)
    content = models.TextField()
    start_date = models.DateTimeField(default=datetime(2021, 9, 12, 0, 0, 0, 0), auto_created=True)
    end_date = models.DateTimeField(default=datetime(2021, 9, 12, 0, 0, 0, 0), auto_created=True)
    place  = models.CharField(default='', max_length=100)