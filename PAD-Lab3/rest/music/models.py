from __future__ import unicode_literals

from django.db import models
from category.models import Category

class Music(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    singer = models.CharField(max_length=255, null=True, blank=True)
    album = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)

    def __unicode__(self):
        return self.title
