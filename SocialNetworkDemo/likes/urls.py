from django.urls import path

from .views import like_post, remove_like

urlpatterns = [
    path('ajax/like_post/', like_post, name='like_post'),
    path('ajax/remove_like/', remove_like, name='like_post')
]