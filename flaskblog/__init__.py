""" Creating a package
__init__.py tells python its a package and runs when file called much like class build.
flask_login - provides user session management for Flask. It lets you log your users in and out in a
            database-independent manner.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy # pip install flask-sqlalchemy
from flask_bcrypt import Bcrypt # pip install flask-bcrypt
from flask_login import LoginManager # pip install flask-login.


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b5331a5f4572740671292b0383de7ff2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) # SQLAlchemy has access to all app attributes

bcrypt = Bcrypt(app)

login_manager = LoginManager(app) # login_manager can now access all app attributes
"""attribs to instance in LoginManager class"""
login_manager.login_view = 'login' # The login_view attribute of the LoginManager object sets the endpoint for the login page.
# Flask-Login will redirect to the login page when an anonymous user tries to access a protected page.
login_manager.login_message_category = 'info' # The message category to flash when a user is redirected to the login
# page. info is blue info alert bootstrap look


from flaskblog import routes


