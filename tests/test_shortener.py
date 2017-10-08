from babyshortener import create_app
from babyshortener.config import TestingConfig
from babyshortener.extensions import db
from babyshortener.utils.bijective import encode, decode, offset
import unittest
from unittest import TestCase
from webtest import TestApp
import sys
from random import randint

# ----------------------------------------------------------------------------------------------------------------------


class ShortenTest(TestCase):

    def setUp(self):
        app = create_app(config=TestingConfig)
        with app.app_context():
            db.create_all()
        self.app = TestApp(app)

# ----------------------------------------------------------------------------------------------------------------------

    def test_valid_url(self):
        valid_url = 'www.google.com'
        resp_1 = self.app.post_json('/shorten_url', dict(url=valid_url))
        self.assertEqual(resp_1.status_int, 201)
        resp_2 = self.app.post_json('/shorten_url', dict(url=valid_url))
        self.assertEqual(resp_1.json["shortened_url"], resp_2.json["shortened_url"])
        redirect = self.app.get(resp_1.json["shortened_url"])
        self.assertEqual(redirect.status_int, 302)
        self.assertEqual(redirect.headers['Location'], 'http://www.google.com')

    def test_invalid_url(self):
        invalid_url = 'foo'
        resp = self.app.post_json('/shorten_url', dict(url=invalid_url), expect_errors=True)
        self.assertEqual(resp.status_int, 400)
        self.assertEqual(resp.json["error"], "Provided URL is invalid")

    def test_empty_payload(self):
        resp = self.app.post_json('/shorten_url', dict(), expect_errors=True)
        self.assertEqual(resp.status_int, 400)
        self.assertEqual(resp.json["error"], "This endpoint only accepts json, no valid json found")

    def test_wrong_arguments(self):
        resp = self.app.post_json('/shorten_url', dict(full_url="www.google.com"), expect_errors=True)
        self.assertEqual(resp.status_int, 400)
        self.assertEqual(resp.json["error"], 'No "url" field found, please fix your query')

    def test_bijective(self):
        rand = randint(0, sys.maxint - offset)
        self.assertEqual(rand, decode(encode(rand)))

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()

# ----------------------------------------------------------------------------------------------------------------------


