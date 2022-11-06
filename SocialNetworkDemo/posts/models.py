from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=1000, null=True, blank=True)
    photo = models.ImageField(upload_to='posts/', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

