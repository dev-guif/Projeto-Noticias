# Generated by Django 4.0.3 on 2022-04-08 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_noticias', '0002_noticias_data_de_publicacao_noticias_titulo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('data_de_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('telefone_celular', models.CharField(blank=True, help_text='Número de telefone no formato (99) 99999-9999', max_length=15, null=True, verbose_name='Telefone celular')),
                ('telefone_fixo', models.CharField(blank=True, help_text='Número de telefone fixo no formato (99) 99999-9999', max_length=14, null=True, verbose_name='Telefone fixo')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
