from babyshortener.models import URL
from babyshortener.extensions import db
from babyshortener.utils.bijective import encode

# ----------------------------------------------------------------------------------------------------------------------


def short_url(full_url):
    instance = URL.query.filter_by(full=full_url).first()
    if instance:
        return instance.short
    session = db.session
    instance = URL(full=full_url)
    session.add(instance)
    session.commit()
    print 'instance id is', instance.id
    short = encode(instance.id)
    print 'after encoding we have', short
    instance.short = short
    session.commit()
    return short

# ----------------------------------------------------------------------------------------------------------------------
