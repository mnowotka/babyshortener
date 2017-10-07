from flask import Blueprint

from babyshortener.blueprints.api.resources.short_url import ShortUrl
from babyshortener.extensions import api

bp = Blueprint('api', __name__)

api.add_resource(ShortUrl, '/shorten_url')
api.init_app(bp)