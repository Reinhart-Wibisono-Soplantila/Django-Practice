from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'judul': 'Kelas Terbuka',
        'subjudul' : 'Dashboard',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About']
        ]
    }
    return render(request, 'index.html', context)
    # return render(request, 'dashboard/index.html', context)
