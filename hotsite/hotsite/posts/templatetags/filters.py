from django import template

register = template.Library()


@register.filter(name='excerpt')
def excerpt(value, arg):
    return value[:arg]
