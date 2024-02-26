from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = 'def1b1d4d5bf91e42aa3f6a0cf1bf20b' ## setting a secret key
app. config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  ## setting the location of the database
## creating sqlalchemy database instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manger = LoginManager(app)

from flaskblog import routes