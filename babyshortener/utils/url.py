"""This file defines a URL validators based on Django ones.

"""

import re

# ----------------------------------------------------------------------------------------------------------------------

""" this regex is different from the one defined by Django because: 
  - in our case protocol is optional
  - I decided that localhost is not a valid URL. This is a design decision that may be changed in future.
"""

url_regex = re.compile(
        r'^((?:http|ftp)s?://)?' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

# ----------------------------------------------------------------------------------------------------------------------


def valid_url(url):
    return bool(url_regex.match(url))

# ----------------------------------------------------------------------------------------------------------------------

""" When doing a redirect, we need a URL with a protocol and using regex seems to be a simplest way of doing that
"""

redirect_url_regex = re.compile(
        r'^(?:http|ftp)s?://.*$', re.IGNORECASE)

# ----------------------------------------------------------------------------------------------------------------------


def valid_url_for_redirect(url):
    return bool(redirect_url_regex.match(url))

# ----------------------------------------------------------------------------------------------------------------------
