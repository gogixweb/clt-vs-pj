from django.db import models

# Create your models here.

class Calculator(models.Model):
    pj = models.TextField(blank=True, null=True)
    clt = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pj


class ContactEmail(models.Model):
    email = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pj
