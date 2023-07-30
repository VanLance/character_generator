from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .models import db as root_db, login_manager, ma
from flask_migrate import Migrate
from .api.auth_routes import api

from char_inventory.helpers import JSONEncoder

from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.config.from_object(Config)

root_db.init_app(app)

migrate = Migrate(app,root_db)

login_manager.init_app(app)
login_manager.login_view = 'signin' #Specify which page to load for Non-Authenticated Users

ma.init_app(app)

app.json_encoder = JSONEncoder
CORS(app)