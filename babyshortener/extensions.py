"""This file imports all the extensions used by the application and creates extensions instances ready to be imported
 from this single place and used in other places.

"""

from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS, cross_origin

db = SQLAlchemy()
api = Api()
cors = CORS()
