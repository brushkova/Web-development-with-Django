from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@stringfilter
@register.filter
def explode(value, separator):
    return value.split(separator)
