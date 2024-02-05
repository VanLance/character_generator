from flask_smorest import Blueprint

bp = Blueprint('characters', __name__, description='ops on characters')

from . import routes