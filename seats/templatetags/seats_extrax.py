from django import template

register = template.Library()


@register.filter
def get_color(available):
    if available:
        return "#227753"
    return "#B72E2E"
