from flask import Blueprint

from flask import render_template, redirect, url_for
from flask import request

from models import db
from models.user import User


auth  = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == "POST":
       username = request.form.get('username')
       password = request.form.get('password')

       if not username or not password:
           return "Fill up all fields", 400
       
       user = User.query.filter_by(username=username).first()

       if user and user.check_password(password):
            return  redirect(url_for('blog.blog_home'))
        
       return 'Wrong password, please try again', 400

    return render_template("auth/login.html")

@auth.route("/register", methods=['GET', 'POST'])
def register():

    if request.method == "POST":
        fullname = request.form.get("fullname")
        username = request.form.get("username")
        email = request.form.get("email")   
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not fullname or not username or not email or not password or not confirm_password:
            return 'All fields are required!', 400
        
        if User.query.filter_by(email=email).first():
            return 'Email already registered!'
        
        if password != confirm_password:
            return 'password are mismatch, please try again!'
        
        new_user = User(fullname=fullname, username=username, email=email, password=password)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template("auth/register.html")
