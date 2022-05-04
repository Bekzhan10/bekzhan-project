from django import template
from poll.models import *
register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter:None):
    if not filter:
        return Genres.objects.all()
    else:
        return Genres.objects.filter(pk=filter)


@register.inclusion_tag('list_categories.html')
def show_categories(sort = None, cat_selected = 0):
    if not sort:
        cats = Poll.objects.all()
    else:
        cats = Poll.objects.order_by(sort)
    return {'cats':cats,'cat_selected':cat_selected}
