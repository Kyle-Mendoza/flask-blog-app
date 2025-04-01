from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_bcrypt import Bcrypt
# models 

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    from .user import User