from flask import Flask
from flask_mail iport Mail
from .config ipmort Config

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)
from app import views
