from flask import Flask, render_template, request
from flask import current_app as app # Alias for the current application
from .models import *

@app.route('/') # Refers to base url path (127.0.0.1:5000)
def home():
    return "<h2>Welcome to AdMatch</h2>"

@app.route("/login", methods=["GET","POST"]) # LOGIN URL
def user_login():  
    if request.method == "POST":

        uname = request.form.get("uname")
        pwd = request.form.get("pwd")

        usr = User.query.filter_by(username=uname, password=pwd).first()
        if usr and usr.role == "0":
            user_summary = fetch_users()
            return render_template("adminDashboard.html", admin=usr.username, users=user_summary)
        elif usr and usr.role == "1":
            return render_template("sponsorDashboard.html", sponsor=usr.username)
        elif usr and usr.role == "2":
            return render_template("influencerDashboard.html", influencer=usr.username)
        else:
            return render_template("login.html", msg="Invalid username or password") # Jinja template

    return render_template("login.html")


@app.route("/signup", methods=["GET","POST"]) # SIGNUP URL
def user_signup():
    if request.method == "POST":

        email = request.form.get("email")
        fname = request.form.get("fullname")
        uname = request.form.get("uname")
        pwd = request.form.get("pwd")
        #role = request.form.get("role")

        usr = User.query.filter_by(username=uname).first()
        if not usr:
            new_user = User(email=email, fullname=fname, username=uname, password=pwd) # Set role for Influencer/Sponsor
            db.session.add(new_user)
            db.session.commit()
            return render_template("login.html", msg="User registered successfully, Kindly log in!")
        else:
            return render_template("signup.html", msg="User already exists, Kindly register again!")
    return render_template("signup.html")

# UDF for fetching all general users
def fetch_users():
    users = User.query.filter_by(role="1").all()
    user_list = {}
    for user in users:
        if user not in user_list.keys():
            user_list[user.id] = [user.username, len(user.lists)]
    return user_list