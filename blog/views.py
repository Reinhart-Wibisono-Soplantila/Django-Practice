from django.shortcuts import render
from django.http import HttpResponse
from .models import post

# Create your views here.
def index(request):
    
    posts = post.objects.all()
    print(posts)
    context = {
        'title' : 'Blog',
        'heading' : 'Blog',
        'subheading' : 'Jurnal Kelas Terbuka',
        'Category' : 'All',
        'posts' : posts,
        # 'banner' : 'blog/img/banner_blog.png',
        # 'app_css' : 'blog/css/style.css',
        # 'nav' : [
        #     ['/', 'Home'],
        #     ['/about', 'About'],
        #     # ['/dashboard', 'Dashboard'],
        #     # ['/contact', 'Contact'],
        #     ['/blog/news', 'News Blog'],
        #     ['/blog/recent', 'Recent Blog'],
        # ]
    }
    return render(request, 'blog/index.html', context)
    # return render(request, 'blog/index.html', context)

def jurnal(request):
    posts = post.objects.filter(category = 'jurnal')
    print(posts)
    context = {
        'title' : 'Blog',
        'heading' : 'Blog',
        'subheading' : 'Jurnal Kelas Terbuka',
        'Category' : 'Jurnal',
        'posts' : posts,
    }
    return render(request, 'blog/index.html', context)

def berita(request):
    posts = post.objects.filter(category = 'berita')
    print(posts)
    context = {
        'title' : 'Blog',
        'heading' : 'Blog',
        'subheading' : 'Jurnal Kelas Terbuka',
        'Category' : 'Berita',
        'posts' : posts,
    }
    return render(request, 'blog/index.html', context)

def gosip(request):
    posts = post.objects.filter(category = 'gosip')
    print(posts)
    context = {
        'title' : 'Blog',
        'heading' : 'Blog',
        'subheading' : 'Jurnal Kelas Terbuka',
        'Category' : 'Gosip',
        'posts' : posts,
    }
    return render(request, 'blog/index.html', context)