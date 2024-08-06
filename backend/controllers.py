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
            user_info = fetch_info(usr.id)
            user_lists = user_info.lists
            return render_template("sponsorDashboard.html", id=user_info.id, name=user_info.username, sponsor=usr.username, lists=user_lists)
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

@app.route("/list/add/<int:user_id>", methods=["GET","POST"]) # ADD LIST URL
def add_list(user_id):
    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("description")
        list_obj = List(title=title, description=desc, user_id=user_id)
        db.session.add(list_obj)
        db.session.commit()
        user_info = fetch_info(user_id)
        return render_template("sponsorDashboard.html", id=user_info.id, name=user_info.username, lists=user_info.lists)

@app.route("/list/edit/<int:user_id>/<int:list_id>", methods=["GET","POST"]) # EDIT LIST URL
def edit_list(user_id, list_id):
    if request.method == "POST":
        new_title = request.form.get("title")
        new_desc = request.form.get("description")
        list_obj = List.query.filter_by(id=list_id).first()
        list_obj.title = new_title
        list_obj.description = new_desc
        db.session.commit()
        user_info = fetch_info(list_obj.user_id)
        return render_template("sponsorDashboard.html", id=user_info.id, name=user_info.username, lists=user_info.lists)

@app.route("/list/delete/<int:list_id>", methods=["GET","POST"]) # DELETE LIST URL
def delete_list(list_id):
    if request.method == "POST":
        pass

# UDF for fetching all general users
def fetch_users():
    users = User.query.filter_by(role="1").all()
    user_list = {}
    for user in users:
        if user not in user_list.keys():
            user_list[user.id] = [user.username, len(user.lists)]
    return user_list

# UDF for fetching user info
def fetch_info(user_id):
    user_info = User.query.filter_by(id=user_id).first()
    return user_info
