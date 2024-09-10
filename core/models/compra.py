from django.db import models

from .user import User
from .livro import Livro

class ItensCompraInline(admin.TabularInline):
    model = ItensCompra
    extra = 1 # Quantidade de itens adicionais

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("usuario", "status")
    search_fields = ("usuario", "status")
    list_filter = ("usuario", "status")
    ordering = ("usuario", "status")
    list_per_page = 25
    inlines = [ItensCompraInline]