from django import template
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.simple_tag
def check_bag(val=None):
    return True if any(d["item_id"] == "13" for d in val) else False
