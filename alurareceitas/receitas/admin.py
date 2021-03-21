from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada',)
    list_display_links = ('id', 'nome_receita')

    #acrescenta um campo de busca no adm no django
    search_fields = ('nome_receita', )
    #acrescenta um filtro no adm no django
    list_filter = ('categoria', )
    #Permite ediçao no campo publicada tela do admin
    list_editable = ('publicada',)
    #Paginando as receitas no Django
    list_per_page = 2


admin.site.register(Receita, ListandoReceitas)
