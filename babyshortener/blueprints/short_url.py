from flask import Blueprint, flash, request
from babyshortener import controllers

bp = Blueprint('babyshortener', __name__)

# ----------------------------------------------------------------------------------------------------------------------


@bp.route('/shorten_url', methods=['POST'])
def shorten_url():
    flash('New entry was successfully posted')
    payload = request.get_json()
    if not payload:
        return '...', 400
    if "shortened_url" not in payload:
        return '...', 400
    full_url = payload['shortened_url']
    short_url = controllers.short_url(full_url)
    return {"shortened_url": short_url}, 201

# ----------------------------------------------------------------------------------------------------------------------
