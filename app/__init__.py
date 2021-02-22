from flask import Flask
from flask_mail import Mail
from .config import Config
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()

app = Flask(__name__)
#app.config.from_object(Config)
app.config['SECRET KEY'] ='Please provide the passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT']= '2525'
app.config['MAIL_USERNAME']= 'Enter your mailtrap username'
app.config['MAIL_PASSWORD']= 'Enter your mailtrap password'

mail = Mail(app)
from app import views
