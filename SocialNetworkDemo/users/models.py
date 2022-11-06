from django.contrib.auth.models import AbstractUser, User
from django.db import models


# class User(AbstractUser):
#     pass

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
