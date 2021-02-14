from django.db import models
from apps.core.models import BestPraticesModel
import datetime


class Author(BestPraticesModel):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nome do Autor')
    email = models.EmailField(blank=False, null=False, verbose_name='Email do Autor')
    
    class Meta:
        verbose_name_plural = 'Autor'

    def __str__(self):
        return self.name


class Article(BestPraticesModel):
    title = models.CharField(max_length=120, blank=False, null=False, verbose_name='Titulo do artigo')
    descripition = models.TextField(blank=False, null=False, verbose_name='Descrição')
    body = models.TextField(blank=False, null=False, verbose_name='Texto')
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name='Autor do texto' )

    class Meta:
        verbose_name_plural = 'Artigo'

    def __str__(self):
        return self.title
