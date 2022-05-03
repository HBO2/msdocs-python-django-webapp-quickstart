from django.db import models

# Create your models here.

class Person(models.Model):
    Name = models.CharField(max_length=64)
    Surname = models.CharField(max_length=64)
    BirthDate = models.DateTimeField()
    Sex = models.CharField(max_length=1)