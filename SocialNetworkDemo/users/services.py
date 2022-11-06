from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import Subscription
from posts.services import PostsServices


class UsersServices:
    def get_user_object(self, user_id):
        return User.objects.get(id=user_id)

    def get_profile(self, request, user_id):
        profile_user = self.get_user_object(user_id=user_id)
        posts = PostsServices().get_posts_by_user(user=profile_user)
        followers_count = len(self.get_followers(user=profile_user))
        subscriptions_count = len(Subscription.objects.filter(follower=profile_user))
        status = self.is_subscribed_status(
            current_user=request.user,
            profile_user=profile_user
        )
        return profile_user, posts, followers_count, subscriptions_count, status

    def get_followers(self, user: User) -> list[User]:
        subscriptions = Subscription.objects.filter(user=user)
        return [subscription.follower for subscription in subscriptions]

    def get_subscriptions(self, user: User) -> list[User]:
        subscriptions = Subscription.objects.filter(follower=user)
        return [subscription.user for subscription in subscriptions]

    def is_subscribed_status(self, current_user: User, profile_user: User) -> str:
        followers = self.get_followers(user=profile_user)
        if current_user in followers:
            status = 'Отписаться'
        else:
            subscriptions = self.get_subscriptions(user=profile_user)
            if current_user in subscriptions:
                status = 'Подписаться в ответ'
            else:
                status = 'Подписаться'
        return status

    def subscribe(self, current_user: User, user: User):
        if current_user == user:
            return HttpResponse(status=403)
        subscription = Subscription.objects.filter(
            user=user, follower=current_user
        )
        if not subscription:
            Subscription.objects.create(
                user=user,
                follower=current_user
            )

    def unsubscribe(self, current_user: User, user: User):
        subscription = Subscription.objects.filter(
            user=user, follower=current_user
        )
        if subscription:
            subscription.delete()

    def search_users(self, search_query: str) -> list[User]:
        possible_users = User.objects.filter(first_name__icontains=search_query)
        possible_users |= User.objects.filter(last_name__icontains=search_query)
        possible_users |= User.objects.filter(username__icontains=search_query)
        possible_users = list(set(possible_users))
        return possible_users
