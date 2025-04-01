import os

from flask import Flask 
from dotenv import load_dotenv

# routes
from routes.main_routes import main
from routes.blog_routes import blog 
from routes.auth_routes import auth 


# models, db, migrate 
from models import db, init_app, bcrypt

load_dotenv() # will load environment variables from .env file

# Intialize the Flask App
app = Flask(__name__)


# Using the DATABASE URL inside the environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Initialize the db and migrate extentions with the App
init_app(app)

# Blueprints
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(blog, url_prefix="/blog")


if __name__ == "__main__":
    app.run(debug=True)
