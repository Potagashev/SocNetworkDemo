from django.contrib.auth.models import User
from django.db.models import QuerySet

from .models import Post, Comment
from django.apps import apps
Subscription = apps.get_model('users', 'Subscription')


class PostsServices:
    def get_post(self, post_id) -> Post:
        return Post.objects.get(id=post_id)

    def get_posts_for_home_page(self, user: User) -> QuerySet[Post]:
        subscriptions = Subscription.objects.filter(follower=user)
        users = [subscription.user for subscription in subscriptions]
        users.append(user)
        return Post.objects.filter(user__in=users).order_by('-pub_date')

    def get_posts_by_user(self, user: User) -> QuerySet[Post]:
        posts = Post.objects.filter(user=user)
        return posts

    def add_post(self, user: User, post_data) -> Post:
        return Post.objects.create(**post_data, user=user)

    def delete_post(self, post_id):
        pass


class CommentsServices:
    def get_comments_by_post(self, post_id) -> QuerySet[Comment]:
        return Comment.objects.filter(post__id=post_id).order_by('-pub_date')

    def add_comment(self, user: User, comment_text, post_id):
        post = Post.objects.get(id=post_id)
        Comment.objects.create(
            user=user,
            text=comment_text,
            post=post
        )
