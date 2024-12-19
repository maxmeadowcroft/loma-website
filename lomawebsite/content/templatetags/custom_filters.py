from django import template
from itertools import groupby
from operator import attrgetter

register = template.Library()

@register.filter
def groupby(value, attr):
    """Groups a queryset by the given attribute."""
    if not value:
        return []
    grouped = groupby(sorted(value, key=attrgetter(attr)), key=attrgetter(attr))
    return [(key, list(group)) for key, group in grouped]
