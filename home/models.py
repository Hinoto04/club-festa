from django.db import models
from django.db.models.enums import IntegerChoices

class User(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    year = models.IntegerField(default=2021)
    number = models.IntegerField()
    regi_date = models.DateField()

    def __str__(self):
        return str(self.number) + self.name