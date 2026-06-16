from django.contrib import admin
from .models import Categorie, Produit, Contact


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom', 'slug', 'icone']
    prepopulated_fields = {'slug': ('nom',)}


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'categorie', 'prix', 'en_stock', 'mis_en_avant', 'date_ajout']
    list_filter = ['categorie', 'en_stock', 'mis_en_avant']
    search_fields = ['nom', 'description']
    prepopulated_fields = {'slug': ('nom',)}
    list_editable = ['en_stock', 'mis_en_avant', 'prix']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['nom', 'telephone', 'date_envoi', 'lu']
    list_filter = ['lu']
    readonly_fields = ['nom', 'telephone', 'message', 'date_envoi']
    list_editable = ['lu']
