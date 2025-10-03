from flask import Flask
from .search import search
from .health import health

def create_marvel_app():
    app = Flask(__name__)


    app.register_blueprint(search)
    app.register_blueprint(health)

    return app


 