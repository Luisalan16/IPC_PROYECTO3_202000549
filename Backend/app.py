from flask import Flask
from routes.rutas import home

app = Flask(__name__)
app.register_blueprint(home)