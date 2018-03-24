from django.shortcuts import render
from .models import Post

def index(request):
    post = Post.objects.filter(title__isnull=False)
    ctx = {'post': post}
    return render(request, 'index.html', ctx)

def article(request):
    post = Post.objects.filter(title__isnull=False)
    ctx = {'post' : post}
    return render(request, 'site_app/article.html', ctx)
