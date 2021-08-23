from django import template

register = template.Library()
@register.filter(name = "cutting")
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    
    """
    return value.replace(arg,"Hell")

# register.filter("cut",cut)
