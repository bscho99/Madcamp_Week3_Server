from django.db import models
import json

# Create your models here.


class User(models.Model):
    userid = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Playlist(models.Model):
    userid = models.CharField(max_length=20)
    title = models.CharField(max_length=30, default="")
    description = models.CharField(max_length=140, default="")
    songs = models.TextField()
    letter = models.CharField(max_length=140, default="")
