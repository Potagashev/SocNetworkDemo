from django.contrib.auth.models import User
from django.db.models import QuerySet

from posts.models import Post
from .models import Like


class LikesServices:
    def __init__(self, post: Post, user: User):
        self.post = post
        self.user = user

    def get_like(self) -> QuerySet[Like]:
        return Like.objects.filter(post=self.post, user=self.user)

    def create_like(self) -> Like:
        if not self.get_like():
            like = Like.objects.create()
            return like

    def remove_like(self):
        self.get_like().delete()

    def get_likers(self) -> list[User]:
        return [like.user for like in Like.objects.filter(post=self.post)]

    def get_likes_count(self):
        return len(Like.objects.filter(post=self.post))
