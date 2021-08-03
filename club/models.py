from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, default='기타')
    isofficial = models.BooleanField(default=False)
    member = models.IntegerField()
    create_date = models.DateTimeField()
    club_master = models.CharField(max_length=20, default='')
    club_teacher = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.name