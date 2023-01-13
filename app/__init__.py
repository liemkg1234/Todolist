from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager


app = Flask(__name__)
# config SECRET_KEY
app.config.from_object(Config)

#Flask-login
login = LoginManager(app)
login.login_view = 'user.login' #dinh vi vi tri trang login cho web

# Database
db = SQLAlchemy(app)
from app.models import User, Note
mirgrate = Migrate(app, db)



def create_app():
    # Blueprint
    from app.note import note
    from app.user import user
    app.register_blueprint(note)
    app.register_blueprint(user)
    # Error
    from app import errors

    #Flask_login
    login_manager = LoginManager()
    login_manager.login_view = 'user.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app