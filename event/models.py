from datetime import datetime
from django.db import models

class Event_Inf(models.Model):
    event_title = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    content = models.TextField()