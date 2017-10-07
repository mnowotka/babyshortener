from flask import Blueprint, flash, request
from flask_restful import Resource
from babyshortener import controllers
from babyshortener.extensions import api

bp = Blueprint('api', __name__)

# ----------------------------------------------------------------------------------------------------------------------


class ShortUrl(Resource):

    def post(self):
        print 'shorten url!'
        flash('New entry was successfully posted')
        payload = request.get_json()
        if not payload:
            print 'no payload'
            return '...', 400
        if "url" not in payload:
            return '...', 400
        full_url = payload['url']
        short_url = controllers.short_url(full_url)
        return {"shortened_url": short_url}, 201

# ----------------------------------------------------------------------------------------------------------------------

api.add_resource(ShortUrl, '/shorten_url')
api.init_app(bp)
