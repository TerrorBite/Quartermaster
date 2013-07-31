from django import template
from django.template.defaultfilters import stringfilter
import urllib


register = template.Library()


@register.simple_tag()
def personal_stats():
    return "No stats."

@register.simple_tag()
def agent_count():
    #TODO: Implementation
    return "0"

@register.simple_tag()
def pending_agent_count():
    #TODO: Implementation
    return "0"
