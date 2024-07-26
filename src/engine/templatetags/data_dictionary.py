from django.template import Library
register = Library()
@register.filter(name='lookup')
def lookup(d, key):
    print("lookup", d,key)    
    value = d.get(key) # simple access here, you can also raise exception in case key is not found
    print(value)
    return value