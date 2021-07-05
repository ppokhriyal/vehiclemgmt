from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


#App Config
app = Flask(__name__)
app.config['SECRET_KEY'] = '878436c0a462c4145fa59eec2c43a66a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_BINDS'] = {'user':'sqlite:///user.db'}
db = SQLAlchemy(app)

#Login Manager
login_manager = LoginManager(app)
login_manager.session_protection = "strong"
login_manager.login_view = 'user_login.login'
login_manager.login_message_category = 'info'

#Import Blueprint routes objects
from vparkingmgmt.user_login.routes import blue
from vparkingmgmt.home.routes import blue
from vparkingmgmt.add_new_vehicle.routes import blue

#Register Blueprint
app.register_blueprint(user_login.routes.blue,url_prefix='/')
app.register_blueprint(home.routes.blue,url_prefix='/')
app.register_blueprint(add_new_vehicle.routes.blue,url_prefix='/')