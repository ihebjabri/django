from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm
from .models import Recipe

# Imports pour CBV et Mixins
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse

# Imports pour PDF
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
try:
    from xhtml2pdf import pisa
    HAS_XHTML2PDF = True
except ImportError:
    HAS_XHTML2PDF = False
from django.contrib import messages
from django.db.models import Q
import datetime


def is_admin(user):
    """
    Vérifie si l'utilisateur est un superuser (admin Django).
    """
    return user.is_authenticated and user.is_superuser


def is_chef(user):
    """
    Vérifie si l'utilisateur appartient au groupe 'chef'.
    """
    return user.is_authenticated and user.groups.filter(name="chef").exists()


def is_normal_user(user):
    """
    Vérifie si l'utilisateur est un utilisateur normal (ni admin ni chef).
    """
    return user.is_authenticated and not is_admin(user) and not is_chef(user)


def get_user_dashboard(user):
    """
    Détermine vers quel dashboard rediriger l'utilisateur selon son rôle.
    Retourne le nom de l'URL du dashboard correspondant.
    """
    if is_admin(user):
        return "dashboard_admin"
    elif is_chef(user):
        return "dashboard_chef"
    else:
        return "dashboard_user"


chef_required = user_passes_test(is_chef, login_url="login")
admin_required = user_passes_test(is_admin, login_url="login")


# ========== MIXINS ==========

class ChefRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return is_chef(self.request.user)

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return is_admin(self.request.user)

class IsOwnerOrAdminMixin(UserPassesTestMixin):
    def test_func(self):
        # Récupère l'objet (la recette) que l'on tente de modifier/supprimer
        obj = self.get_object()
        # Autoriser si l'utilisateur est le propriétaire OU s'il est admin
        return obj.user == self.request.user or is_admin(self.request.user)

# ========== AUTH VIEWS (Restores FBV for simplicity) ==========

def login_page(request):
    if request.user.is_authenticated:
        return redirect(get_user_dashboard(request.user))
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(get_user_dashboard(request.user))
    else:
        form = AuthenticationForm(request)
    return render(request, "registration/login.html", {"form": form})

def register_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect(get_user_dashboard(request.user))
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def logout_user(request):
    logout(request)
    return redirect("login")

# ========== CBV VIEWS ==========

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list.html"
    context_object_name = "recipes"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        # Tri par date (jour)
        return queryset.order_by('day')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class RecipeCreateView(LoginRequiredMixin, ChefRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/form.html"
    success_url = reverse_lazy('recipes')
    extra_context = {'title': 'Créer une recette'}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, IsOwnerOrAdminMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/form.html"
    success_url = reverse_lazy('recipes')
    extra_context = {'title': 'Modifier une recette'}

class RecipeDeleteView(LoginRequiredMixin, IsOwnerOrAdminMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes')
    
    def get(self, request, *args, **kwargs):
        # Permettre la suppression par simple GET pour simplifier (optionnel, sinon faut POST)
        return self.post(request, *args, **kwargs)

class PlannerView(LoginRequiredMixin, TemplateView):
    template_name = "dashboards/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # On passe les événements en JSON pour FullCalendar
        events = []
        recipes = Recipe.objects.all()
        for recipe in recipes:
            events.append({
                'title': recipe.name,
                'start': recipe.day.isoformat(), # YYYY-MM-DD
                'url': reverse('update_recipe', args=[recipe.id]) if is_chef(self.request.user) else '#',
                'color': '#28a745'
            })
        context['events_json'] = events
        return context


@login_required(login_url="login")
def pdf_page(request):
    """
    Génère un PDF de toutes les recettes pour la semaine.
    """
    if not HAS_XHTML2PDF:
        messages.error(request, "PDF generation is not available. Please install xhtml2pdf library.")
        return redirect('recipes')

    # Tri par date
    recipes = Recipe.objects.all().order_by('day')

    template_path = 'recipes/pdf_template.html'
    context = {'recipes': recipes}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="planning_repas.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url="login")
@admin_required
def promote_to_chef(request, user_id):
    """
    Promeut un utilisateur au rang de Chef (ajoute au groupe 'chef').
    """
    from django.contrib.auth.models import User
    target_user = get_object_or_404(User, id=user_id)
    chef_group, created = Group.objects.get_or_create(name='chef')
    
    target_user.groups.add(chef_group)
    messages.success(request, f"L'utilisateur {target_user.username} est maintenant Chef !")
    
    return redirect('dashboard_admin')


# ========== DASHBOARDS SELON LES RÔLES ==========

@login_required(login_url="login")
@admin_required
def dashboard_admin(request):
    """
    Dashboard réservé aux administrateurs (superusers).
    Permet de gérer les utilisateurs, groupes et recettes.
    """
    from django.contrib.auth.models import User
    
    total_users = User.objects.count()
    total_recipes = Recipe.objects.count()
    total_chefs = User.objects.filter(groups__name="chef").distinct().count()
    recent_recipes = Recipe.objects.all().order_by("-id")[:5]
    
    today_users = User.objects.all().order_by("-date_joined")
    
    context = {
        "total_users": total_users,
        "total_recipes": total_recipes,
        "total_chefs": total_chefs,
        "recent_recipes": recent_recipes,
        "users": today_users, # Pour la liste et promotion
    }
    return render(request, "dashboards/dashboard_admin.html", context)


@login_required(login_url="login")
def dashboard_chef(request):
    """
    Dashboard réservé aux chefs.
    Permet de gérer les recettes (création, modification, suppression).
    """
    # Vérifier que l'utilisateur est bien chef
    if not is_chef(request.user):
        return redirect("dashboard_user")
    
    user_recipes = Recipe.objects.filter(user=request.user).order_by("-id")
    all_recipes = Recipe.objects.all().order_by("-id")[:10]
    total_recipes = Recipe.objects.filter(user=request.user).count()
    
    context = {
        "user_recipes": user_recipes,
        "all_recipes": all_recipes,
        "total_recipes": total_recipes,
    }
    return render(request, "dashboards/dashboard_chef.html", context)


@login_required(login_url="login")
def dashboard_user(request):
    """
    Dashboard pour les utilisateurs normaux.
    Permet de consulter les recettes disponibles.
    """
    all_recipes = Recipe.objects.all().order_by("day", "name")
    
    context = {
        "recipes": all_recipes,
    }
    return render(request, "dashboards/dashboard_user.html", context)
