import os
basedir = os.path.abspath(os.path.dirname(__file__))
NAME_DB = 'app.db'

class Config(object):
    SECRET_KEY = os.environ.get('SECKET_KEY') or 'UDontKnow'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, NAME_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False