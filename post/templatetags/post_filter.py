import datetime
from django import template

register = template.Library()

@register.filter()
def username(value):
    vs = value.name.split(' ')
    if len(vs) <= 1:
        return vs[0]
    else:
        return vs[-1]

@register.filter()
def club(value):
    if len(value)>5:
        s = ""
        vs = value.split(' ')
        if len(vs[0])>5:
            for i in value.split(' '):
                s += i[0]
            if s>5:
                s = s[:5]
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