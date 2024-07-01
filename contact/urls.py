from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
    path('form2/', views.form2, name='form2'),
    path('form1/', views.form1, name='form1'),
    path('form/', views.create, name='create'),
    path('delete/<int:delete_id>', views.delete, name='delete'),
    path('', views.index, name='index'),
]

