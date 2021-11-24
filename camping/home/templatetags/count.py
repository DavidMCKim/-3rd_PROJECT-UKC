from django import template

register = template.Library()

@register.filter
def ranges(count=101):
    return range(0, count)
