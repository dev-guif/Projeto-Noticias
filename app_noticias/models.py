from django.db import models
from django.forms import CharField, DateField
from django.contrib.auth.models import User

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField('Nome', max_length=128)
    data_de_nascimento = models.DateField('Data de Nascimento', blank=True, null=True)
    telefone_celular = models.CharField('Telefone celular', max_length=15, 
                                        help_text='Número de telefone no formato (99) 99999-9999', 
                                        null=True, blank=True)
    telefone_fixo = models.CharField('Telefone fixo', max_length=14,
                                        help_text='Número de telefone fixo no formato (99) 99999-9999',
                                        null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)
    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.nome
        
class Noticias(models.Model):
    titulo = models.CharField("Título", max_length=128, blank=True, null=True)
    conteudo = models.TextField("Conteúdo")
    data_de_publicacao = models.DateField("Data de publicação", blank=True, null=True)
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.titulo

