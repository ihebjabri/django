from django import template

register = template.Library()


@register.simple_tag
def get_user_dashboard_url(user):
    """
    Retourne l'URL du dashboard correspondant au rôle de l'utilisateur.
    """
    if not user.is_authenticated:
        return None
    
    if user.is_superuser:
        return 'dashboard_admin'
    elif user.groups.filter(name='chef').exists():
        return 'dashboard_chef'
    else:
        return 'dashboard_user'

