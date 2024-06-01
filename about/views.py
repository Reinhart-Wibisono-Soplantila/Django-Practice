from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'title' : 'About',
        'heading' : 'About',
        'subheading' : 'Tentang Kelas Terbuka',
        # 'banner' : 'about/img/banner_about.png',
        # 'app_css' : 'about/css/style.css',
        # 'nav' : [
        #     ['/', 'Home'],
        #     ['/blog', 'Blog'],
        #     # ['/dashboard', 'Dashboard'],
        #     # ['/contact', 'Contact'],
        #     ['/blog/news', 'News Blog'],
        #     ['/blog/recent', 'Recent Blog'],
        # ]
    }
    # return render(request, 'about/index.html', context)
    return render(request, 'about/index.html', context)