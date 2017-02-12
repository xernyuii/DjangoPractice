from django.db import models

# Create your models here.
class Person(model.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()



