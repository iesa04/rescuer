from django.template import Library
register = Library()
@register.filter(name='count_iems')
def count_iems(lst):
    return len(lst)