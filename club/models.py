from django.db import models

class Club(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    member = models.IntegerField()
    create_date = models.DateTimeField()