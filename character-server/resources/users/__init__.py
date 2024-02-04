from flask_smorest import Blueprint

bp = Blueprint('users', __name__, description='Ops on Users')

from . import routes, auth_routes