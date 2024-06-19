from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.index, name='index'),
    # path('jurnal/', views.jurnal),
    # path('berita/', views.berita),
    # path('gosip/', views.gosip),
    # path('<str:categoryInput>/', views.filter),
    path('category/<str:categoryInput>/', views.categoryPost, name='category'),
    path('post/<str:slugInput>/', views.detailPost, name='detail')
]
