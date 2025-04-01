from models import db 
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    password = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)