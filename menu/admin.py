from django.contrib import admin
from .models import Menu

# Register your models here.

class menuAdmin(admin.ModelAdmin):
    list_display = ("item","size","temp","price")

admin.site.register(Menu,menuAdmin)
