"""This file provides an implementation of API Resource for shortening urls.

You may wonder why I used flask_restful Resource and not a regular Flask route.
The reason if flexibility - in future we may want to add new serialisation formats or some arguments to parse.
Inheriting from the Resource will make it easier.

Todo:
    * Improve validation (extract to a separate method)
    * Better error handling

"""

from flask import request
from flask_restful import Resource
from babyshortener import controllers
from babyshortener.utils.url import valid_url
from werkzeug.local import LocalProxy
from flask import current_app

logger = LocalProxy(lambda: current_app.logger)

# ----------------------------------------------------------------------------------------------------------------------


class ShortUrl(Resource):

    def post(self):

        # I assume data is given as JSON but it may be as well application/x-www-form-urlencoded, this can be handled
        # in future.
        payload = request.get_json()

        # Validation goes here, it should be done in a separate place in code.
        if not payload:
            logger.warning('no payload')
            return {"error": 'This endpoint only accepts json, no valid json found'}, 400
        if "url" not in payload:
            logger.warning('bad payload')
            return {"error": 'No "url" field found, please fix your query'}, 400
        full_url = payload['url']
        if not valid_url(full_url):
            return {"error": 'Provided URL is invalid'}, 400

        # Now that we are sure we are dealing with a valid URL we can actually shorten it.
        hash = controllers.short_url(full_url)
        short_url = request.url_root + hash
        return {"shortened_url": short_url}, 201

# ----------------------------------------------------------------------------------------------------------------------

