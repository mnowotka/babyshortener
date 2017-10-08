"""This file defines data models used by controllers. Currently we only have ORM models but this may change in future.
Actually, currently there is only a single model but I can imaging more:

- Model to gather stats
- Model to represent adds to be injected during the redirection if we are going that way
- Model to register users
- many more...

"""

from babyshortener.extensions import db

# ----------------------------------------------------------------------------------------------------------------------


class URL(db.Model):
    """
    A model to represent the only entity of our app - the URL.
    It has a primary key, full version of the url (unique since we don't want repetitions) and fully searchable
    because we search in records using that field. And a short user friendly identifier generated directly from the
    primary key.
    """
    id = db.Column(db.Integer, primary_key=True)
    full = db.Column(db.String(80), unique=True, nullable=False, index=True)
    short = db.Column(db.String(120), nullable=True)

# ----------------------------------------------------------------------------------------------------------------------

