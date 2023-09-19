from django import template

register = template.Library()


@register.simple_tag()
def media_url(image):
    return f'/media/{image}'

