from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Topic(models.Model):
    topic = models.CharField(max_length=250)
    board = models.ForeignKey(Board, related_name = 'topics', on_delete = models.CASCADE)
    creator = models.ForeignKey(User, related_name = 'topics', on_delete = models.CASCADE) 
    created_date = models.DateTimeField(auto_now_add = True)

class Post(models.Model):
    essay = models.TextField(max_length=800)
    topic = models.ForeignKey(Topic, related_name = 'posts', on_delete = models.CASCADE)
    creator = models.ForeignKey(User, related_name = 'posts', on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)