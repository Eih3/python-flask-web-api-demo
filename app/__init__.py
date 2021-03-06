#!/usr/bin/python
# -*- coding: utf-8 -*-

# ------- IMPORT DEPENDENCIES ------- 
from flask import Flask
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS, cross_origin

# ------- IMPORT LOCAL DEPENDENCIES ------- 
import os
from config import app_config


# ------- REGISTERS ------- 

# REGISTER ENVIRONMENT VARIABLES
# os.environ["FLASK_CONFIG"] = "development" or $ export FLASK_CONFIG=development
config_name = os.getenv('FLASK_CONFIG', 'default')

# REGISTER APPLICATION  
app = Flask(__name__, instance_relative_config=True)

# REGISTER CONFIGURATION TYPE    
app.config.from_object(app_config[config_name])
# REGISTER SENSITIVE CONFIG KEYS from the secret instance folder
app.config.from_pyfile(app_config[config_name].SECRET_CONFIG)

# REGISTER DATABASE
db = SQLAlchemy(app)

# REGISTER CSRF FORM PROTECTION
# CSRF protection requires a secret key to securely sign the token. 
# By default this will use the Flask app's SECRET_KEY. If you'd like to use a separate token you can set WTF_CSRF_SECRET_KEY.
csrf = CSRFProtect(app)

# REGISTER SESSION
# Session(app)
sess = Session()
sess.init_app(app)

# REGISTER LOGGING
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# REGISTER BOOTSTRAP
Bootstrap(app)

# REGISTER CORS
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
# CORS(app, resources={r"/*": {"origins": "*"}})
# CORS(app) # then add @cross_origin() in specific route controller
# Or allow only from specific origin : 
CORS(app, resources={r"/*": {"origins": ["http://spa.quickandclean.org", "http://app.quickandclean.org"]}})
logging.getLogger('flask_cors').level = logging.INFO

# ------- IMPORT LOCAL DEPENDENCIES AFTER REGISTERING -------  
#To solve the problem from circular import, place the other imports which are dependent on 'db' and app below app== and db=SQLAlchemy(app).

# ------- LAST REGISTER MODULES WITH BLUEPRINTS -------  
from . import modules, controllers, helpers


# REGISTER BLUEPRINTS
from modules.users import users_page
app.register_blueprint(users_page, url_prefix='/users')

from modules.auth import auth_page
app.register_blueprint(auth_page, url_prefix='/auth')

from modules.sections import sections_page
app.register_blueprint(sections_page, url_prefix='/sections')

from modules.items import items_page
app.register_blueprint(items_page, url_prefix='/items')

from modules.events import events_page
app.register_blueprint(events_page, url_prefix='/events')

from modules.addresses import addresses_page
app.register_blueprint(addresses_page, url_prefix='/addresses')

from modules.assets import assets_page
app.register_blueprint(assets_page, url_prefix='/assets')

from modules.orders import orders_page
app.register_blueprint(orders_page, url_prefix='/orders')

from modules.payments import payments_page
app.register_blueprint(payments_page, url_prefix='/payments')

from modules.payments import creditcards_page
app.register_blueprint(creditcards_page, url_prefix='/creditcards')

from modules.localization import localization_service
app.register_blueprint(localization_service, url_prefix='/localization')

from modules.home import home_page
app.register_blueprint(home_page, url_prefix='/home')

from modules.contact import contact_page
app.register_blueprint(contact_page, url_prefix='/contact')



