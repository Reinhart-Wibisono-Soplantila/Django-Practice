from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'judul' : 'Kelas Terbuka',
        'contributor' : 'Zaki',
        'subjudul' : 'Blog',
        'nav' : [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/dashboard', 'Dashboard'],
            ['/contact', 'Contact'],
            ['/blog/news', 'News Blog'],
            ['/blog/recent', 'Recent Blog'],
        ]
    }
    # return render(request, 'index.html', context)
    return render(request, 'index.html', context)

def recent(request):
    context = {
        'judul' : 'Recent Blog',
        'contributor' : 'Ilham',
        'subjudul' : 'recent post'
    }
    return render(request, 'blog/index.html', context)

def news(request):
    context = {
        'judul' : 'News Blog',
        'contributor' : 'Izzah',
        'subjudul' : 'news blog'
    }
    return render(request, 'blog/index.html', context)