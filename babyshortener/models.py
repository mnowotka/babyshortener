from babyshortener.extensions import db

# ----------------------------------------------------------------------------------------------------------------------


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full = db.Column(db.String(80), unique=True, nullable=False, index=True)
    short = db.Column(db.String(120), nullable=True)

# ----------------------------------------------------------------------------------------------------------------------

