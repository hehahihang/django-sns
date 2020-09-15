from django.shortcuts import render
from posts.models import Post, Comment
import pdb

def home(request):
    context = {
        'user': request.user,
        'posts': Post.objects.all().order_by("-created_at"),
        'comments': Comment.objects.all()
    }
    return render(request, 'home.html', context)