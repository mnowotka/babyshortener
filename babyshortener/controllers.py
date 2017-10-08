"""This file defines controllers that interact with models.
Currently we have a single kind of controller that talks to a DB via SQLalchemy ORM.

I can imagine other strategies:

 - using NoSQL stuff like MongoDB or Redis
 - in memory solution (of limited use when scaling is important)
 
So this file may be actually converted into a module that defines some abstract class and a set of concrete
implementations (backends), each one using different persistency layer.
The choice of a backend would be up to the user, specified in config.
 
Again, I don't have time for that right now. 

"""

from babyshortener.models import URL
from babyshortener.extensions import db
from babyshortener.utils.bijective import encode, decode

# ----------------------------------------------------------------------------------------------------------------------


def short_url(full):
    """
    Takes a url to be shortened, looks for it into a database.
    If a record is found, it returns a short identifier from a matched record.
    Of no results are found in DB it creates a new record, saves it to get a new autoincremented primary key and
    converts this primary key into a short string that is returned as identifier and saved in a newly created record.
    
    :param full: a full URL to be shortened
    :return: short identifier
    """
    instance = URL.query.filter_by(full=full).first()
    if instance:
        return instance.short
    session = db.session
    instance = URL(full=full)
    session.add(instance)
    session.commit()
    short = encode(instance.id)
    instance.short = short
    session.commit()
    return short

# ----------------------------------------------------------------------------------------------------------------------


def full_url(short):
    """
    Decodes a short identifier into primary key. Uses this key to look up the database.
    If a record is found returns a full url.
    If there was an error encountered during decoding or no record is found returns None.
    
    :param short: short identifier
    :return: full url belonging to the identifier
    """
    try:  # This is provided by the user, we can't be sure if we are able to decode it...
        pk = decode(short)
    except:  # pokemon error handling here is quite lame, we may actually validate the user-provided content instead
        return None
    instance = URL.query.filter_by(id=pk).first()
    if not instance:
        return
    return instance.full

# ----------------------------------------------------------------------------------------------------------------------
