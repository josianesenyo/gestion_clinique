# gestion_clinique/templatetags/custom_tags.py
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter # S'assure que la valeur est une chaîne
def startswith(value, arg):
    """Vérifie si la chaîne 'value' commence par 'arg'."""
    if value is None:
        return False
    return value.startswith(arg)




