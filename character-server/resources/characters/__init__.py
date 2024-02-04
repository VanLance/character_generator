from flask_smorest import Blueprint

bp = Blueprint('characters', __name__, url_prefix='/post', description='ops on characters')

from . import routes