import os

from flask import Flask 
from dotenv import load_dotenv
from flask_login import LoginManager

# routes
from routes.main_routes import main
from routes.blog_routes import blog 
from routes.auth_routes import auth 


# models, db, migrate 
from models import db, init_app, bcrypt
from models.user import User

load_dotenv() # will load environment variables from .env file

# Intialize the Flask App
app = Flask(__name__)


# Using the DATABASE URL inside the environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

# Initialize the db and migrate extentions with the App
init_app(app)

# Flask-Login 
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

# Blueprints
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(blog, url_prefix="/blog")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    


if __name__ == "__main__":
    app.run(debug=True)
