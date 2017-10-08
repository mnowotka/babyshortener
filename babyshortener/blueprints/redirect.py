"""This file defines a second blueprint for this application.

The blueprint is all about redirecting.
You may ask why 'shorten_url' is expressed as API Resource and 'redirect' is just an ordinary route.
The reason is that the 'redirect' doesn't fulfill the definition of resource, specifically, it doesn't have
a well defined name, instead it can accept any short url.

It may happen that the short url will actually be 'shorten_url' string but the probability of such an event is 
extrememly low.

There is also a question about blueprints precedence - it is critical for this application that shorten_url route has
a higher precedence than redirect and currently there is nothing in the code that would ensure it. This is because
redirect only supports GET and shorten_url only supports POST. In future this ma change so this issue should be solved.

Another problem is that the application accepts a URL without a protocol as perfectly valid while when doing a 
redirect we have to specify some protocol. This of course is very convenient for our users but we may thing
if there is a better way than assuming HTTP when no protocol is given.

Todo:
    * Solve the precedence issue

"""

import json
from flask import Blueprint, Response, redirect
from babyshortener.controllers import full_url
from babyshortener.utils.url import valid_url_for_redirect

# ----------------------------------------------------------------------------------------------------------------------

bp = Blueprint('redirect', __name__)


# ----------------------------------------------------------------------------------------------------------------------

@bp.route('/<short>', methods=['GET'])
def redirect_url(short):
    full = full_url(short)
    if not full:
        msg = "We couldn't find a link for the URL ({0}) you requested".format(short)
        return Response(content_type='application/json', response=json.dumps({'error': msg}), status=404)
    if not valid_url_for_redirect(full):  # no protocol specified...
        full = 'http://' + full  # assuming http
    return redirect(full, code=302)


# ----------------------------------------------------------------------------------------------------------------------
