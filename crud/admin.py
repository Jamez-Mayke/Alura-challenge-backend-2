from django.contrib import admin
from crud.models import expenses, revenues

class revenues_config(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)

admin.site.register(revenues, revenues_config)

class expenses_config(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)

admin.site.register(expenses, expenses_config)