from django.shortcuts import render
from django import forms

# penulisan import dari file lokal bisa dilakukan dengan dua cara 
# 1. berarti nulis forms.namaclassnya
from . import forms
# 2. langsung nama kelasnya
from .forms import ContactForm
from .forms_contact import ContactForms

# Create your views here.

def index(request):
    contact_form = ContactForms()
    context ={
        'title' : 'Contact',
        'heading' : 'Contact',
        'subheading' : 'Jurnal Kelas Terbuka',
        'Contact_Form' : contact_form
    }
    # Derbugging
    print(request.POST)
    return render(request, 'contact.html', context)

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