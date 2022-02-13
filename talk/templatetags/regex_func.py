import re
from django import template
register = template.Library()


@register.filter
def regex_func(context):
    match = re.compile("1_[0-9]{2}_[1-4]")
    return match.fullmatch(context)


@register.filter
def get_name(arr, index):
    if len(arr) != 0:
        return arr[int(index)-1].name
    return ""


@register.filter
def get_contact(arr, index):
    if len(arr) != 0:
        return arr[int(index)-1].contact
    return ""


@register.filter()
def split(value):
    return value.split("\\")
