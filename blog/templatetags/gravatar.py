import hashlib
import urllib
from urllib.parse import quote_plus
from django import template
from django.utils.safestring import mark_safe

"""
Method to create and register custom template tag found in django docs
https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/
Method suggested in gravatar docs:
https://en.gravatar.com/site/implement
"""
register = template.Library()


# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=40):
    email_bytes = email.lower().encode('utf-8')
    # default gravatar placeholder if user doesn't have registered gravatar
    default = "https://res.cloudinary.com/ddvsgi5xw/image/upload/"
    "v1677666590/gravatar_default_g4uhzf.png"
    return "https://www.gravatar.com/avatar/%s?%s" % (
        hashlib.md5(email_bytes).hexdigest(), urllib.parse.quote_plus(
            'd={}&s={}'.format(default, size)))


# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar:150 }}
@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email, size)
    return mark_safe('<img src="{}" width="{}" height="{}" '
                     'alt="User profile picture">'.format(url, size, size))
