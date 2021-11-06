from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from club.models import Club

class Event(models.Model):
    title = models.CharField(default='', max_length=100) #행사명
    host = models.ForeignKey(Club, on_delete=CASCADE) #주최자명(외래키), Club 참조
    content = models.TextField() #행사내용
    
    start_date = models.DateTimeField(default=datetime.now(), auto_created=True) #행사시작일
    end_date = models.DateTimeField(default=datetime.now(), auto_created=True) #행사끝나는일
    
    place  = models.CharField(default='', max_length=100) #장소