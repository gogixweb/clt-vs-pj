from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Calculator(models.Model):
    pj = models.IntegerField(blank=True, null=True)
    clt = models.IntegerField(blank=True, null=True)

class Email(models.Model):
    address = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length = 200, blank=True)
    content = models.CharField(max_length = 800, blank=True)
