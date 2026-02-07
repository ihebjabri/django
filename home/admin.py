from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group

from .models import Recipe, Category, Rating, CookingStep, RecipeLike


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Administration for recipe categories"""
    list_display = ('name', 'slug', 'icon', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Administration des recettes dans l'interface Django admin.
    """
    list_display = ('name', 'day', 'user', 'difficulty', 'preparation_time', 'created_at', 'get_rating')
    list_filter = ('day', 'user', 'difficulty', 'categories')
    search_fields = ('name', 'description')
    filter_horizontal = ('categories',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    def get_rating(self, obj):
        """Display average rating"""
        avg = obj.average_rating()
        count = obj.rating_count()
        if count > 0:
            return f"{avg:.1f}★ ({count} reviews)"
        return "No ratings"
    get_rating.short_description = 'Rating'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Administration for recipe ratings"""
    list_display = ('recipe', 'user', 'score', 'created_at')
    list_filter = ('score', 'created_at')
    search_fields = ('recipe__name', 'user__username', 'review')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(CookingStep)
class CookingStepAdmin(admin.ModelAdmin):
    """Administration for cooking steps"""
    list_display = ('recipe', 'step_number', 'title', 'duration_minutes')
    list_filter = ('recipe',)
    search_fields = ('recipe__name', 'title', 'instruction')
    ordering = ('recipe', 'step_number')


@admin.register(RecipeLike)
class RecipeLikeAdmin(admin.ModelAdmin):
    """Administration for recipe likes"""
    list_display = ('recipe', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('recipe__name', 'user__username')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


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
