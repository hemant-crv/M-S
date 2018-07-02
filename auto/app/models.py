# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class detail(models.Model):
    name = models.CharField(max_length=250)
    employee_id = models.IntegerField()
    project = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    duration = models.IntegerField()
    access = models.CharField(max_length=250)
    status = models.CharField(max_length=250,default='pending')

    def __str__(self):
        return self.name + '-' +self.access+ '-' +unicode(self.employee_id)
