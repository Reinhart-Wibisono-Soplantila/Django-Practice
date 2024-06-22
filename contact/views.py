from django.shortcuts import render
# from django import forms
from django.http import HttpResponseRedirect

# penulisan import dari file lokal bisa dilakukan dengan dua cara 
# 1. berarti nulis forms.namaclassnya
from . import forms
# 2. langsung nama kelasnya
from .forms import ContactForm
from .forms_contact import ContactForms
from .models import contactModel

# Create your views here.

def index(request):
    posts = contactModel.objects.all()
    context ={
        'title' : 'Contact',
        'heading' : 'Contact',
        'subheading' : 'Jurnal Kelas Terbuka',
        'post' : posts
    }
    # Derbugging
    return render(request, 'contact/index.html', context)

def create(request):
    contact_form = ContactForms(request.POST or None)
    error = None
    if request.method == 'POST':
        if contact_form.is_valid():
            contactModel.objects.create(
                NamaLengkap = contact_form.cleaned_data.POST['NamaLengkap'],
                # tanggal_lahir = request.POST['tanggal_lahir'],
                Jenis_Kelamin = contact_form.cleaned_data.POST['Jenis_Kelamin'],
                Email = contact_form.cleaned_data.POST['Email'],
                Alamat = contact_form.cleaned_data.POST['Alamat'],
                # Agree = request.POST['Agree'],
                # Kode_Pos = request.POST['Kode_Pos'],
                # Kota = request.POST['Kota'],
                # Provinsi = request.POST['Provinsi'],
            )
            return HttpResponseRedirect('/contact/')
        else:
            error = contact_form.errors
            
    context ={
        'title' : 'Contact',
        'heading' : 'Contact',
        'subheading' : 'Jurnal Kelas Terbuka',
        'Contact_Form' : contact_form,
        'error' : error
    }
    # Derbugging
    print(request.POST)
    return render(request, 'contact/form.html', context)

def form2(request):
    
    context = {
        'title' : 'form Biasa',
        }
    
    # Debugging
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