import markdown
from django import template
from django.utils.safestring import mark_safe
from datetime import date

register = template.Library()

@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))

@register.filter()
def strf(value:date):
    return value.strftime("%d")