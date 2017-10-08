from babyshortener.models import URL
from babyshortener.extensions import db
from babyshortener.utils.bijective import encode, decode

# ----------------------------------------------------------------------------------------------------------------------


def short_url(full):
    instance = URL.query.filter_by(full=full).first()
    if instance:
        return instance.short
    session = db.session
    instance = URL(full=full)
    session.add(instance)
    session.commit()
    print 'instance id is', instance.id
    short = encode(instance.id)
    print 'after encoding we have', short
    instance.short = short
    session.commit()
    return short

# ----------------------------------------------------------------------------------------------------------------------


def full_url(short):
    try:  # This is provided by the user, we can't be sure if we are able to decode it...
        pk = decode(short)
    except:  # pokemon error handling here is quite lame, we may actually validate the user-provided content instead
        return None
    instance = URL.query.filter_by(id=pk).first()
    if not instance:
        return
    return instance.full

# ----------------------------------------------------------------------------------------------------------------------
