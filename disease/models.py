from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class Data(models.Model):
    iso_code = models.CharField(max_length=3, unique=True)
    data = models.JSONField()

# helper class for using the 5 countries requested
class Country(models.Model):
    iso_code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
