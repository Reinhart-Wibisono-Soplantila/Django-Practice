from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.index, name='index'),
    path('form1/', views.form1, name='form1'),
    path('form2/', views.form2, name='form2'),
]

