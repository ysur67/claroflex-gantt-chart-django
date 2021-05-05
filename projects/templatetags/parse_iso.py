from django.template import Library
import datetime
from django.conf import settings

register = Library()


@register.simple_tag(takes_context=False)
def parse_datetime(value):
    datetime_format = settings.REST_FRAMEWORK.get('DATETIME_FORMAT')
    if isinstance(value, datetime.datetime):
        return datetime.datetime.strftime(value, datetime_format)
    elif isinstance(value, str):
        return value
