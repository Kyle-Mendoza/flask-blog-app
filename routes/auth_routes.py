from flask import Blueprint 

from flask import render_template, redirect, url_for, request



auth  = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    
    if request.method == "POST":
        return "This request is post" 

    return render_template("auth/login.html")

@auth.route("/register", methods=['GET', 'POST'])
def register():
    pass