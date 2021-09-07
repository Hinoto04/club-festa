import datetime
import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def title(value):
    return value[:25]

@register.filter()
def username(value):
    vs = value.name.split(' ')
    if len(vs) <= 1:
        return vs[0]
    else:
        return vs[-1]

@register.filter()
def club(value):
    print(value)
    if len(value)>6:
        s = ""
        vs = value.split()
        if len(vs[0])>6:
            for i in value.split():
                s += i[0]
            if len(s)>6:
                s = s[:6]
        else:
            s = vs[0]
        return s
    else:
        return value

@register.filter()
def dt(value:datetime):
    now = datetime.datetime.now()
    if value.date() == now.date():
        return value.strftime('%H:%M')
    else:
        return value.strftime('%m.%d')
    
@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))