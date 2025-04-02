from flask import Blueprint

from flask import render_template, request

from models import db
from models.post import Post

from flask_login import login_required, current_user

blog = Blueprint('blog', __name__)


@blog.route("/", methods=["GET", "POST"])
@login_required
def blog_home():

    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        
        if not title or not description:
            return "make sure you have title and description for your post"

        # new_post = Post(title=title, description=description, user_id=user.id)
        return "GOOD"

    return render_template("blog/index.html")

@blog.route("/<int:id>")
def show_blog(id):
    return f"This is one of Blog Post {id}"

@blog.route("/<int:id>/edit")
def edit_blog(id):
    return f"This is one of the Edit Blog post {id}"

@blog.route("/<int:id>/delete")
def delete_blog(id):
    return f"Deleting this blog post id {id}"


    
