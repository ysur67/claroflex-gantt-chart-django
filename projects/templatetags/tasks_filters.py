from django import template

register = template.Library()

@register.filter
def filter_active(tasks):
    return tasks.filter(actual_close_date__isnull=True)
