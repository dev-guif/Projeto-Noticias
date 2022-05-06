from unicodedata import name
from django.contrib import admin
from django.urls import path
from app_noticias.views import homeView, noticia_detalhes, noticias_resumo_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resumo_noticias/', noticias_resumo_template, name='resumo_noticias'),
    path('noticias/<int:noticia_id>/', noticia_detalhes, name='detalhes'),
    path('', homeView, name='home')
    ]