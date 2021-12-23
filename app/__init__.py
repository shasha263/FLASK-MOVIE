from flask import Flask
from config import Config

from .movie.routes import movie

app=Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(movie)


from . import routes
