from django.shortcuts import render
from .models import Post


def home(request):
    all_post = Post.objects.all()

    return render(request, 'index.html', {'all_post_list': all_post})


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'post_list.html', {'post_list': post_list})