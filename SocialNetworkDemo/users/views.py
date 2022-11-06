from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login

from .forms import UserSignInForm, UserSignUpForm
from .services import UsersServices


def sign_in(request):
    if request.user.is_authenticated:
        redirect('home')
    if request.method == 'POST':
        form = UserSignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserSignInForm()
    return render(request, 'users/sign_in.html', {'form': form})


def sign_up(request):
    if request.user.is_authenticated:
        redirect('home')
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserSignUpForm()
    return render(request, 'users/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('sign_in')


def profile(request, user_id):
    profile_user, posts, followers_count, subscriptions_count, status\
        = UsersServices().get_profile(request, user_id)

    context = {
        'profile_user': profile_user,
        'posts': posts,
        'followers_count': followers_count,
        'subscriptions_count': subscriptions_count,
        'status': status,
    }
    return render(request, 'users/profile.html', context)


def subscribe(request, user_id):
    users_services = UsersServices()
    users_services.subscribe(
        current_user=request.user,
        user=users_services.get_user_object(user_id)
    )
    return redirect('profile', user_id=user_id)


def unsubscribe(request, user_id):
    users_services = UsersServices()
    users_services.unsubscribe(
        current_user=request.user,
        user=users_services.get_user_object(user_id=user_id)
    )
    return redirect('profile', user_id=user_id)


def show_subscriptions(request, user_id):
    users_services = UsersServices()
    user = users_services.get_user_object(user_id=user_id)
    subscriptions = users_services.get_subscriptions(user=user)
    return render(
        request,
        "users/show_subscriptions.html",
        context={'subscriptions': subscriptions}
    )


def show_followers(request, user_id):
    users_services = UsersServices()
    user = users_services.get_user_object(user_id=user_id)
    followers = users_services.get_followers(user=user)
    return render(
        request,
        "users/show_followers.html",
        context={'followers': followers}
    )


def search_users(request):
    if request.POST:
        search_query = request.POST.get('search_query')
        possible_users = UsersServices().search_users(search_query=search_query)
        return render(
            request,
            "users/search_users.html",
            {'possible_users': possible_users}
        )
    else:
        return render(
            request,
            "users/search_users.html"
        )
