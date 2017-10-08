#!/usr/bin/env python

"""This script when called directly runs a dubug server.
But it also exposes a WSGI application object to be used by servers like gunicorn.

"""


__author__ = 'mnowotka'
from babyshortener import create_app

app = create_app()

# ----------------------------------------------------------------------------------------------------------------------


def main(conf_path=None):
    app.run(debug=True)

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()

else:
    application = app

# ----------------------------------------------------------------------------------------------------------------------
