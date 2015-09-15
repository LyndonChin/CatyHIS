from django.db import models

# Create your models here.

class Person(models.Model):
    order = models.CharField(max_length=5)
    team = models.CharField(max_length=100)
    team_no = models.IntegerField()
    name = models.CharField(max_length=10)
    sex = models.IntegerField()
    age = models.IntegerField()
    community = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
