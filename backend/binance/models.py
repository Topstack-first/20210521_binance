from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=70, blank=False, default='')
    lastname = models.CharField(max_length=70, blank=False, default='')
    age = models.IntegerField(blank=False, default=1)
    address = models.CharField(max_length=70, blank=False, default='')
    copyrightby = models.CharField(max_length=70, blank=False, default='')