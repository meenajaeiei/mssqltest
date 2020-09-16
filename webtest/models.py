from django.db import models

class sqlserverconn(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()