from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
import datetime


class User(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User name: %r email: %r>' % (self.name, self.email)
