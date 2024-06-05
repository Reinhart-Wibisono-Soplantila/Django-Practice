from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('jurna;/', views.jurnal),
    path('berita/', views.berita),
    path('gosip/', views.gosip)
]
