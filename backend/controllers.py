from flask import Flask, render_template
from flask import current_app as app # Alias for the current application

@app.route('/') # Refers to base url path (127.0.0.1:5000)
def home():
    return "<h2>Welcome to Kanban Board</h2>"

@app.route("/login") # Refers to login url path
def user_login():
    return render_template("login.html")

@app.route("/signup") # Refers to register url path
def user_signup():
    return render_template("signup.html")