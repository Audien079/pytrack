from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Param filter will take url kwargs and append page after kwargs
    """
    text = context["request"].GET.copy()
    for key, value in kwargs.items():
        text[key] = value
    for key in [key for key, value in text.items() if not value]:
        del text[key]
    return text.urlencode()


@register.filter
def hyphened_number(value):
    """
    Add hyphens to a phone number
    """
    return f"{value[:3]}-{value[3:6]}-{value[6:]}"
