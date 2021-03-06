from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    com_date = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Post(models.Model):
    caption = models.CharField(max_length=255)
    upl_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to = 'photos/', blank = True)
    comment = models.ForeignKey(Comment)



    def __str__(self):
        return self.caption


class Connect(models.Model):
    follower = models.ForeignKey(User, related_name='follower')
    following = models.ForeignKey(User, related_name='following')


    def __str__(self):
        return self.follower.username + ' : '+self.following.username
