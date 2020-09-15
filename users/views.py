from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Profile, Post

@login_required
def follow_toggle(request, id):
    user = request.user

    followed_user = get_object_or_404(User, pk=id)
    is_follower = user.profile in followed_user.profile.followers.all()

    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('home')



@login_required
def profile_page(request):
    posts = Post.objects.filter(user=request.user).order_by("created_at")
    return render(request, 'users/mypage.html', {'posts': posts})

def following_list(request):
    followings = request.user.profile.followings.all()
    return render(request, 'users/followings.html',{'followings':followings})

def follower_list(request):
    followers = request.user.profile.followers.all()
    return render(request, 'users/followers.html',{'followers':followers})
