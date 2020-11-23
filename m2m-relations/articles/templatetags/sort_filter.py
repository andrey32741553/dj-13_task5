from django import template

register = template.Library()


@register.filter
def sorting(value):
    ordering = 'name'
    return value.order_by(ordering)
