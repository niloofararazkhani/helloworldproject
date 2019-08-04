# -*- coding: utf-8 -*-
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    page_num = models.IntegerField()
    is_first = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

# Create your models here.
