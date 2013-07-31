from django import template
from django.template.defaultfilters import stringfilter
import urllib


register = template.Library()


@register.simple_tag()
def personal_stats():
    return "No stats."
