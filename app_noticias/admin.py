from django.contrib import admin
from .models import Noticias, Pessoa, Tag

@admin.register(Noticias)
class NoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(Pessoa)
class NoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class NoticiaAdmin(admin.ModelAdmin):
    pass