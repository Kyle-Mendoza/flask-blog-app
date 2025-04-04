from flask import Blueprint

from flask import render_template, request, redirect, url_for

from models import db
from models.post import Post
from models.user import User

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

        new_post = Post(title=title, description=description, user_id=current_user.id)

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('blog.blog_home'))

    posts = Post.query.all()

    return render_template("blog/index.html", posts=posts)

@blog.route("/<int:id>")
@login_required
def show_blog(id):
    post = Post.query.get_or_404(id)
    return render_template('blog/show.html', post=post)

@blog.route("/<int:id>/edit", methods=['GET', 'POST'])
@login_required
def edit_blog(id):
    post = Post.query.get_or_404(id)
    
    if request.method == "POST":
        post.title = request.form['title']
        post.description = request.form['description']


        db.session.commit()
        
        return redirect(url_for('blog.show_blog', id=post.id))
    
    return render_template('blog/edit.html', post=post)

@blog.route("/<int:id>/delete", methods=['POST'])
@login_required
def delete_blog(id):
    post = Post.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('blog.blog_home'))


    
