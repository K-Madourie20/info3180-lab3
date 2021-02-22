import os
set MAIL_SERVER ="smtp.mailtrap.io"
set MAIL_PORT=465
set MAIL_USERNAME="ee97be7d59de58"
set MAIL_PASSWORD="a7e201ef4ebd3c"
set SECRET_KEY="qwerty123"

class Config(object):
    """Base Config Object""" 
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'loacalhost'
    MAIL_POST = os.environ.get('MAIL_PORT') or '25'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False


