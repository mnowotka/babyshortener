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
