from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
    # return HttpResponse('Hello World')
    context = {
        'judul' : 'Halaman Admin',
        'contributor' : 'Rein',
    }
    return render(request, 'index.html', context)