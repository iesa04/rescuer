from django import template
register = template.Library()
@register.filter()
def to_int(value):
   if str(value) == 'None':
      return -1
   else:
      return int(value)      