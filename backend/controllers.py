from flask import Flask, render_template, request
from flask import current_app as app # Alias for the current application

@app.route('/') # Refers to base url path (127.0.0.1:5000)
def home():
    return "<h2>Welcome to Kanban Board</h2>"

@app.route("/login", methods=["GET","POST"]) # Refers to login url path
def user_login():
    if request.method == "POST":
        uname = request.form.get("uname")
        pwd = request.form.get("pwd")
        if uname == "admin" and pwd == "admin":
            return "Login Success"
        else:
            return "Login Failed"
    return render_template("login.html")

@app.route("/signup", methods=["GET","POST"]) # Refers to register url path
def user_signup():
    return render_template("signup.html")