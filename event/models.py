from datetime import date
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from club.models import Club
from datetime import date

class Event(models.Model):
    title = models.CharField(default='', max_length=100) #행사명
    
    host = models.ForeignKey(Club, on_delete=CASCADE) #주최자명(외래키), Club 참조
    
    content = models.TextField() #행사내용
    
    start_date = models.DateField(default=date(2000, 1, 1), auto_created=True) #행사시작일
    end_date = models.DateField(default=date(2000, 1, 1), auto_created=True) #행사끝나는일
    
    place  = models.CharField(default='', max_length=100) #장소
    
    def __str__(self):
        return self.title