from django.urls import path
from . import views


urlpatterns = [
    path('', views.WebsiteHome, name='Home'),
    path('Chapinchat/', views.Upload, name='Dashboard'),
    path('ObtenerUsuarios/', views.getUsers , name='listaUsers'),
    path('Creador/', views.Creator, name='creador'),
    path('Documentacion/', views.Documentation, name='document')

]