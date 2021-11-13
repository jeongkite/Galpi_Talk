import re
from django import template
register = template.Library()


@register.filter
def regex_func(context):
    match = re.compile("1_[0-9]{2}_[1-4]")
    return match.fullmatch(context)
