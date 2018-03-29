from django.shortcuts import render
from .models import Post, SECTIONS

def index(request):
    post = Post.objects.all()
    ctx = {'post': post, 'sections': SECTIONS}
    return render(request, 'site_app/index.html', ctx)

def article(request):
    post = Post.objects.get(id=request.GET['id'])
    all_posts = Post.objects.filter(title__isnull=False)
    ctx = {'post' : post, 'all_posts': all_posts, 'sections': SECTIONS}
    return render(request, 'site_app/article.html', ctx)

def bysection(request):
    sect_articles = Post.objects.filter(section=request.GET['section'])
    print(sect_articles)
    all_posts = Post.objects.all()
    ctx = {'sect_articles': sect_articles,'all_posts': all_posts,
           'sections': SECTIONS}
    return render(request, 'site_app/section.html', ctx)
