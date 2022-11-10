import json

from django.http import HttpResponse
from django.shortcuts import render


from .services import LikesServices
from posts.services import PostsServices


def like_post(request, post_id):
    if request.POST:
        likes_services = LikesServices(
            post=PostsServices().get_post(post_id),
            user=request.user
        )
        if likes_services.create_like():
            return HttpResponse(content=json.dumps(likes_services.get_likes_count()), content_type='application/json', )
        else:
            return HttpResponse(status=403, content={'details': 'post is already liked'})
    else:
        return HttpResponse(status=405, content={'details': f'{request.method} method not allowed'})


def remove_like(request, post_id):
    if request.POST:
        likes_services = LikesServices(
            post=PostsServices().get_post(post_id),
            user=request.user
        )
        likes_services.remove_like()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405, content={'details': f'{request.method} method not allowed'})