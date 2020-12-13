from flask import Flask
from flask_sqlalchemy import Model, SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '2b3b0653a9d3c42948bd5edce8fd84cb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #creating a local SQlite Database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Removes tracking of changes to the database
db = SQLAlchemy(app) #Assigning our database to SQLAlchemey
bcrypt = Bcrypt(app) ##Flask library used to hash passwords
login_manager = LoginManager(app) #Flask library to manage login on our web application
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'

from cardealer import routes

