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


@register.filter
def gravatar_url(email, size=40):
    """
    Return only the URL of the gravatar
    associated with email address.
    Parameter size is measured in pixels.
    """
    email_bytes = email.lower().encode('utf-8')
    # default gravatar placeholder if user doesn't have registered gravatar
    default = "https://res.cloudinary.com/ddvsgi5xw/image/upload/"
    "v1677666590/gravatar_default_g4uhzf.png"
    return "https://www.gravatar.com/avatar/%s?%s" % (
        hashlib.md5(email_bytes).hexdigest(), urllib.parse.quote_plus(
            'd={}&s={}'.format(default, size)))


@register.filter
def gravatar(email, size=40):
    """
    Returns an image tag with the gravatar
    Template use:  {{ email|gravatar:150 }}
    """
    url = gravatar_url(email, size)
    return mark_safe('<img src="{}" width="{}" height="{}" '
                     'alt="User profile picture">'.format(url, size, size))
