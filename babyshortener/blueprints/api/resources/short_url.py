from flask import flash, request
from flask_restful import Resource
from babyshortener import controllers
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
            return '...', 400
        if "url" not in payload:
            logger.warning('bad payload')
            return '...', 400
        full_url = payload['url']
        hash = controllers.short_url(full_url)
        short_url = request.url_root + hash
        return {"shortened_url": short_url}, 201

# ----------------------------------------------------------------------------------------------------------------------

