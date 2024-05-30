from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
    # return HttpResponse('Hello World')
    context = {
        'judul' : 'Kelas Terbuka',
        'contributor' : 'Rein',
        'subjudul' : 'Home',
        'banner' : 'img/banner_home.png',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/dashboard', 'Dashboard'],
            ['/contact', 'Contact'],
        ]
    }
    return render(request, 'index.html', context)