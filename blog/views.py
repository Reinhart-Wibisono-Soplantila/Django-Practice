from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'judul' : 'Halaman Blog',
        'contributor' : 'Zaki'
    }
    # return render(request, 'index.html', context)
    return render(request, 'blog/index.html', context)

def recent(request):
    context = {
        'judul' : 'Recent Blog',
        'contributor' : 'Ilham'
    }
    return render(request, 'blog/index.html', context)

def news(request):
    context = {
        'judul' : 'News Blog',
        'contributor' : 'Izzah'
    }
    return render(request, 'blog/index.html', context)