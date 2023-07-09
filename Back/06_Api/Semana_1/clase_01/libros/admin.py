from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display =["titulo","autor","precio"]
    search_fields = ["titulo","precio"]

# admin.site.register(Libro)
