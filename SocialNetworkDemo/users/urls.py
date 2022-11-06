from django.urls import path

from .views import sign_up, sign_in, sign_out, profile, show_followers, show_subscriptions, subscribe, unsubscribe, \
    search_users

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('profile/<int:user_id>', profile, name='profile'),
    path('sign_out/', sign_out, name='sign_out'),
    path('show_followers/<int:user_id>', show_followers, name='show_followers'),
    path('show_subscriptions/<int:user_id>', show_subscriptions, name='show_subscriptions'),
    path('subscribe/<int:user_id>', subscribe, name='subscribe'),
    path('unsubscribe/<int:user_id>', unsubscribe, name='unsubscribe'),
    path('search/', search_users, name='search_users'),
]
