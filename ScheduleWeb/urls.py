"""
URL configuration for ScheduleWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # URL Dynamic
    # path('<int:tahun>/<int:bulan>/<int:hari>', views.tanggal),
    # path('<int:input>/', views.angka),
    # path('page/<str:page>/', views.link), #slug
    # path('angka/<int:input>/', views.angka),
    
    # namespacing memakai namespace dari url utama ke include atau app lain
    # name untuk alias
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('about/', include('about.urls', namespace='about')),
    path('', views.index, name='index'),
    path('form1/', views.form1, name='form1'),
    path('form2/', views.form2, name='form2'),
    path('admin/', admin.site.urls),
]
