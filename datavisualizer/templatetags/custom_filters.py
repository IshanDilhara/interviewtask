from django import template

register = template.Library()

@register.filter
def getattr(obj, attr_name):
    """Gets an attribute from an object by name."""
    return getattr(obj, attr_name, None)  # Return None if attribute doesn't exist
