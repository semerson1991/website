# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=450)
    youtube_video_identifier = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=450)
    width = models.IntegerField(default=300, blank=False, null=False)
    height = models.IntegerField(default=300, blank=False, null=False)
    url = models.URLField()

    def __str__(self):
        return self.title
