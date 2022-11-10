from django.shortcuts import render, redirect

from .forms import CreatePostForm
from .services import PostsServices, CommentsServices


def home(request):
    if request.user.is_authenticated:
        posts = PostsServices().get_posts_for_home_page(request=request)
        return render(request, 'posts/home.html', context={'posts': posts})
    else:
        return redirect('sign_in')


def get_post(
    request,
    post_id,
):
    post = PostsServices().get_post(post_id=post_id)
    comments = CommentsServices().get_comments_by_post(post_id=post_id)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'posts/details.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = CreatePostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post_data = form.cleaned_data
            PostsServices().add_post(request=request, post_data=post_data)
            return redirect('profile', user_id=request.user.id)
    else:
        form = CreatePostForm()
    return render(request, 'posts/add_post.html', context={'form': form})


def add_comment(request, post_id):
    comment_text = request.POST.get('comment_text')
    CommentsServices().add_comment(
        request=request,
        comment_text=comment_text,
        post_id=post_id
    )
    return redirect('post_details', post_id=post_id)
