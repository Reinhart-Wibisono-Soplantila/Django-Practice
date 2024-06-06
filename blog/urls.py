from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('jurnal/', views.jurnal),
    # path('berita/', views.berita),
    # path('gosip/', views.gosip),
    path('<str:categoryInput>/', views.filter),
    path('post/<str:slugInput>/', views.singlePost)
]
