from django.http import HttpResponse
from django.shortcuts import render
from django import forms

# penulisan import dari file lokal bisa dilakukan dengan dua cara 
# 1. berarti nulis forms.namaclassnya
from . import forms
# 2. langsung nama kelasnya
from .forms import ContactForm

# method view
def index(request):
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

def form2(request):
    
    context = {
        'title' : 'form Biasa',
        }
    if request.method == 'POST':
        print('ini adalah method post')
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']
    else:
        print('Ini adalah method get')
        
    print(request.POST)
    return render(request, 'form2.html', context)

def form1(request):
    contact_form = ContactForm()
    context = {
        'title' : 'Class form',
        'contact_form' : contact_form
        }
    if request.method == 'POST':
        print('ini adalah method post')
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']
    else:
        print('Ini adalah method get')
    
    # print(request.POST)
    return render(request, 'form1.html', context)

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