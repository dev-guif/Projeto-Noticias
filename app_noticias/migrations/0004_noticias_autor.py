# Generated by Django 4.0.3 on 2022-04-08 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0003_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_noticias.pessoa'),
        ),
    ]
