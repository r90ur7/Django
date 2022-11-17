from django.contrib import admin
from django.contrib import admin
from produto.models import Cores, Produtos

class CorAdmin(admin.ModelAdmin):
    list_display= ['cor']
    ordering= ['-cor']   
    search_fields= ['cor']
    list_filter = ['cor',]
    list_editable = []

admin.site.register(Cores, CorAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'cor', 'quantidade','preco']
    ordering = ['-produto']
    search_fields = ['produto']
    list_filter = ['produto']
    list_editable = ['preco', 'quantidade']

admin.site.register(Produtos, ProdutoAdmin)

# Register your models here.
