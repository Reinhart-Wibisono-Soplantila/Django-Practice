from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
    # return HttpResponse('Hello World')
    context = {
        'title' : 'Kelas Terbuka',
        'heading' : 'Selamat Datang',
        'subheading' : 'di Kelas Terbuka',
        'banner' : 'img/banner_home.png',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/admin', 'Admin'],
            # ['/contact', 'Contact'],
        ],
    }
    return render(request, 'index.html', context)

# def form(request):
#     context = {'title' : 'form'}
    
#     if request.method == 'POST':
#         print('ini adlaah method post')
#         context['nama'] = request.POST['nama']
#         context['alamat'] = request.POST['alamat']

def angka(request, input):
    heading = "<h1> ANGKA </h1>"
    stri = heading + str(input)
    return HttpResponse(stri)

# ada dua cara untuk melakukan return jika banyak input url
# Cara 1
def tanggal(request, tahun, bulan, hari):
    tahun = 'tahun' + str(tahun)
    bulan = 'bulan' + str(bulan)
    hari = 'hari' + str(hari)
    heading = "<h1> Tanggal </h1>"
    stri = heading + tahun + '<br>' + bulan + '<br>' + hari
    return HttpResponse(stri)
    
# Cara 2
def tanggal(request, **kwargs):
    tahun = kwargs.get('tahun')
    bulan = kwargs.get('bulan')
    hari = kwargs.get('hari')
    heading = "<h1> Tanggal </h1>"
    str2 = "{} / {} / {}".format(tahun, bulan, hari)
    return HttpResponse(str2)

def link(request, page):
    str = "<h1> Page Link {}</h1>".format(page)
    return HttpResponse(str)