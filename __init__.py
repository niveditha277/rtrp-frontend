from flask import Flask # type: ignore

app = Flask(__name__)
app.config.from_object('config')

from app import routes
