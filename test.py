from flask import Flask
from flask_pymongo import Pymongo


app = Flask(__name__)

app.route('/')
def first():
    return 'hey there'
