from django.contrib import admin
from filmes.models import Filmes, Generos
from .models import Filmes, Generos

class GenerosAdmin(admin.ModelAdmin):
    list_display= ['genero']
    ordering= ['-genero']   
    search_fields= ['genero']
    list_filter = ['genero',]
    list_editable = []

admin.site.register(Generos, GenerosAdmin)

class FilmesAdmin(admin.ModelAdmin):
    list_display = ['filme', 'genero', 'quantidade','preco']
    ordering = ['-filme']
    search_fields = ['filme']
    list_filter = ['filme']
    list_editable = ['preco', 'quantidade']

admin.site.register(Filmes, FilmesAdmin)

# Register your models here.
