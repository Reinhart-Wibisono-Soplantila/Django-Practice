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

def categoryPost(request, categoryInput):
    posts = post.objects.filter(category=categoryInput)
    categories = post.objects.values('category').distinct()
    print(categories)
    context = {
        'title' : 'Blog',
        'heading' : 'Blog',
        'subheading' : 'Jurnal Kelas Terbuka',
        'categories' : categories,
        'posts' : posts,
    }
    # return HttpResponse(posts.title)
    return render(request, 'blog/categoryPost.html', context)

# slug itu unik sehingga hanya ada satu atau memakai get
# masalah adalah tidak bisa dilakukan for karena object melalui get adlaah noniterable
def detailPost(request, slugInput):
    posts = post.objects.get(slug=slugInput) #queryset
    context = {
        'title' : 'Blog',
        'heading' : 'Blog',
        'subheading' : 'Jurnal Kelas Terbuka',
        'posts' : posts,
    }
    # return HttpResponse(posts.title)
    return render(request, 'blog/singlePost.html', context)



# def jurnal(request):
#     posts = post.objects.filter(category = 'jurnal')
#     print(posts)
#     context = {
#         'title' : 'Blog',
#         'heading' : 'Blog',
#         'subheading' : 'Jurnal Kelas Terbuka',
#         'Category' : 'Jurnal',
#         'posts' : posts,
#     }
#     print(posts)
#     return render(request, 'blog/index.html', context)

# def berita(request):
#     posts = post.objects.filter(category = 'berita')
#     print(posts)
#     context = {
#         'title' : 'Blog',
#         'heading' : 'Blog',
#         'subheading' : 'Jurnal Kelas Terbuka',
#         'Category' : 'Berita',
#         'posts' : posts,
#     }
#     return render(request, 'blog/index.html', context)

# def gosip(request):
#     posts = post.objects.filter(category = 'gosip')
#     print(posts)
#     context = {
#         'title' : 'Blog',
#         'heading' : 'Blog',
#         'subheading' : 'Jurnal Kelas Terbuka',
#         'Category' : 'Gosip',
#         'posts' : posts,
#     }
#     return render(request, 'blog/index.html', context)

# def filter(request, categoryInput):
#     posts = post.objects.filter(category=categoryInput)
#     context = {
#         'title' : 'Blog',
#         'heading' : 'Blog',
#         'subheading' : 'Jurnal Kelas Terbuka',
#         'Category' : 'Gosip',
#         'posts' : posts,
#     }
#     return render(request, 'blog/index.html', context)