from django import template

register = template.Library()


@register.filter
def get_color(available):
    if available:
        return "#59B343"
    return "#FF3D00"
