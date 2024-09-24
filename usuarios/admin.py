from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio', 'created_at', 'updated_at', 'active']
    search_fields = ['username', 'email']
    list_filter = ['created_at', 'updated_at', 'active']
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    fields = ['username', 'password', 'email', 'bio', 'profile_picture', 'birth_date', 'phone', 'address', 'city', 'state',]