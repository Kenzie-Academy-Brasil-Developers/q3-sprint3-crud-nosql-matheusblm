from flask import Flask
from app import routes
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["kenzie"]

def create_app():
    app = Flask(__name__)
    routes.init_app(app)
    return app