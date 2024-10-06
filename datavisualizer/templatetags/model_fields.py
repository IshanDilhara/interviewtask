from django import template
from django.db.models import Field

register = template.Library()

@register.filter
def get_fields(model):
    return [field for field in model._meta.get_fields() if not isinstance(field, Field)]