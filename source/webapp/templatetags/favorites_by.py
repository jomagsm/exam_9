from django import template

register = template.Library()

@register.filter
def favorites_by(obj, user):
    print(obj)
    return obj.favorites_by(user)