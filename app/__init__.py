from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('app.config')
mongo = PyMongo(app)
jwt = JWTManager(app)


from app.routes import auth_routes, user_routes
