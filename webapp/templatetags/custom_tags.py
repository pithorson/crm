from django import template
from django.forms import CheckboxInput

register = template.Library()

@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, CheckboxInput)