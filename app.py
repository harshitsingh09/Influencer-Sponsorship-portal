# Controller file for the application
from flask import Flask

app = None # Global variable

def init_app():
    kanban_app = Flask(__name__) # Object of Flask class
    kanban_app.debug = True
    kanban_app.app_context().push()
    print("App initialized")
    return kanban_app

app = init_app()
from backend.controllers import *
if __name__ == "__main__":
    app.run()