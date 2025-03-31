from flask import Blueprint

from flask import render_template

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("user/index.html") 

@main.route("/about")
def about():
    return render_template("user/about.html") 

@main.route("/contact")
def contact():
    pass