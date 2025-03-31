from flask import Blueprint

from flask import render_template 

blog = Blueprint('blog', __name__)


@blog.route("/")
def blog_home():
    return render_template("blog/index.html")

