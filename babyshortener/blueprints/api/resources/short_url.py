from flask import flash, request
from flask_restful import Resource
from babyshortener import controllers
from babyshortener.utils.url import valid_url
from werkzeug.local import LocalProxy
from flask import current_app

logger = LocalProxy(lambda: current_app.logger)

# ----------------------------------------------------------------------------------------------------------------------


class ShortUrl(Resource):

    def post(self):
        flash('New entry was successfully posted')
        payload = request.get_json()
        if not payload:
            logger.warning('no payload')
            return {"error": 'This endpoint only accepts json, no valid json found'}, 400
        if "url" not in payload:
            logger.warning('bad payload')
            return {"error": 'No "url" field found, please fix your query'}, 400
        full_url = payload['url']
        if not valid_url(full_url):
            return {"error": 'Provided URL is invalid'}, 400
        hash = controllers.short_url(full_url)
        short_url = request.url_root + hash
        return {"shortened_url": short_url}, 201

# ----------------------------------------------------------------------------------------------------------------------

