from django.urls import path
from . import views

urlpatterns = [
    # CBV List
    path('', views.RecipeListView.as_view(), name='recipes'),
    
    # Auth
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_user, name='logout'),
    
    # Dashboards
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/chef/', views.dashboard_chef, name='dashboard_chef'),
    path('dashboard/user/', views.dashboard_user, name='dashboard_user'),
    path('dashboard/planner/', views.PlannerView.as_view(), name='planner'), # Ajout Planner
    
    # CRUD Recettes
    path('recipes/create/', views.RecipeCreateView.as_view(), name='create_recipe'),
    path('update_recipe/<int:pk>/', views.RecipeUpdateView.as_view(), name='update_recipe'), # pk is standard for CBV
    path('delete_recipe/<int:pk>/', views.RecipeDeleteView.as_view(), name='delete_recipe'),
    
    path('pdf/', views.pdf_page, name='pdf'),
    path('promote/<int:user_id>/', views.promote_to_chef, name='promote_to_chef'),
]
