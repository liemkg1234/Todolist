"""
# Create db
flask db init
# Updaete db
flask db migrate -m "Set notNull in Column"
flask db upgrade

# Create new user
from app import db
from app.models import User
u = User('liem123','liem123@gmail.com')
u.hash_pw('123')
db.session.add(u)
db.session.commit()
"""

from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(356), nullable=False)
    notes = db.relationship('Note')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def hash_pw(self, password): # Hash password
        self.password_hash = generate_password_hash(password, method='sha256')

    def check_pw(self, password): # Check pw and hash_pw
        return check_password_hash(self.password_hash, password)


# SELECT ID FROM USER
@login.user_loader
def load_user(id):
    return User.query.get(int(id))



class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, data, user_id):
        self.data = data
        self.user_id = user_id


