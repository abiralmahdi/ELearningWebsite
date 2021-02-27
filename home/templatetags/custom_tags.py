from django import template
import ast

register = template.Library()

@register.filter # register the template filter with django
def get_string_as_list(value): # Only one argument.
    """Evaluate a string if it contains []"""
    return ast.literal_eval(value)

register.filter('get_string_as_list', get_string_as_list)