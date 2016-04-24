from __future__ import unicode_literals

from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(User, default=1)
    name = models.CharField(max_length=250)
    tagline = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    
    company = models.ForeignKey(Company, default=1)
    first = models.CharField(max_length=250)
    last = models.CharField(max_length=250)
    phone = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.comment
