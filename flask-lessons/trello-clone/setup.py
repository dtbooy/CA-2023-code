from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt 
from flask_jwt_extended import JWTManager
from os import environ

app = Flask(__name__)

# Insert DB connection string into app.config
app.config[
    'SQLALCHEMY_DATABASE_URI'] = environ.get("DB_URI")
# Create JWT Token Secret Key
app.config['JWT_SECRET_KEY'] = environ.get("JWT_KEY")

# app connections
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app) 
jwt = JWTManager(app)