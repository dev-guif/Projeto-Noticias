from django.shortcuts import render
from django.http import Http404
from .models import Noticias

def noticias_resumo_template(request):
    total = Noticias.objects.count()
    return render(request, 'app_noticias/resumo.html', {'total': total})

def noticia_detalhes(request, noticia_id):
    try:
        noticia = Noticias.objects.get(pk=noticia_id)
    except Noticias.DoesNotExist:
        raise Http404('Notícia não encontrada!')
    return render(request, 'app_noticias/detalhes.html', {'noticia': noticia})    

def homeView(request):
    return render(request, 'app_noticias/home.html')