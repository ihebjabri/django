from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group

from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Administration des recettes dans l'interface Django admin.
    """
    list_display = ('name', 'day', 'user', 'description')
    list_filter = ('day', 'user')
    search_fields = ('name', 'description', 'day')
    ordering = ('day', 'name')


# Personnalisation de l'admin pour les utilisateurs et groupes
# On garde l'admin User standard mais on ajoute des infos supplémentaires
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    """
    Admin personnalisé pour les utilisateurs avec affichage des groupes (rôles).
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'date_joined', 'get_groups')
    
    def get_groups(self, obj):
        """Affiche les groupes (rôles) de l'utilisateur"""
        return ", ".join([group.name for group in obj.groups.all()]) or "Aucun"
    get_groups.short_description = 'Rôles'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """
    Administration des groupes (rôles) comme 'chef', 'client', etc.
    Permet à l'admin de créer et gérer les rôles.
    """
    list_display = ('name', 'get_user_count')
    search_fields = ('name',)
    
    def get_user_count(self, obj):
        """Affiche le nombre d'utilisateurs dans ce groupe"""
        return obj.user_set.count()
    get_user_count.short_description = 'Nombre d\'utilisateurs'
