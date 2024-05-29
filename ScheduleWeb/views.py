from django.http import HttpResponse
from django.shortcuts import render

# method view
def index(request):
    # return HttpResponse('Hello World')
    return render(request, 'index.html')

def about(request):
    return HttpResponse('abouttt')