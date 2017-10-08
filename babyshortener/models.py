"""This file defines data models used by controllers. Currently we only have ORM models but this may change in future.
Actually, currently there is only a single model but I can imaging more:

- Model to gather stats
- Model to represent adds to be injected during the redirection if we are going that way
- Model to register users
- many more...

TODO:
* make full and short url lengths configurable

"""

from babyshortener.extensions import db


# Currently Chrome browser is the most liberal in terms of maximum allowed URL
# (https://stackoverflow.com/questions/417142/what-is-the-maximum-length-of-a-url-in-different-browsers)
# In practice this can be much smaller (~2000) due to Apache limitations.
CHROME_MAX_URL_LENGTH = 32779

# Since hash is currently base62-encoded 10 characters give 839299365868340224 possible values.
# The biggest integer value that SQLite can handle (I assume this is the worst db backend that can be used here) is
# 9223372036854775807, then this is the safest value as 62^11 = 52036560683837093888 > 9223372036854775807.
MAX_HASH_LENGTH = 10

# ----------------------------------------------------------------------------------------------------------------------


class URL(db.Model):
    """
    A model to represent the only entity of our app - the URL.
    It has a primary key, full version of the url (unique since we don't want repetitions) and fully searchable
    because we search in records using that field. And a short user friendly identifier generated directly from the
    primary key.
    """
    id = db.Column(db.Integer, primary_key=True)
    full = db.Column(db.String(CHROME_MAX_URL_LENGTH), unique=True, nullable=False, index=True)
    short = db.Column(db.String(MAX_HASH_LENGTH), nullable=True)

# ----------------------------------------------------------------------------------------------------------------------

