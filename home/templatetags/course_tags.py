from django import template
import math

register= template.Library()

@register.simple_tag
def discount_calculation(price,discount):
    if not discount or discount is 0:
        return price
    selling_price = price - (price * discount/100)
    return math.floor(selling_price)




