from flask_login import UserMixin

from models import db, bcrypt 

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    password = db.Column(db.String(120), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True, cascade="all, delete")

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User id={self.id} fullname={self.fullname} username={self.username}>"