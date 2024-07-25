# Controller file for the application
from flask import Flask
from backend.models import *

app = None # Global variable

def init_app():
    AdMatch_app = Flask(__name__) # Object of Flask class
    AdMatch_app.debug = True
    AdMatch_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AdMatch.db' # Database URI
    AdMatch_app.app_context().push() # Direct access to the other modules
    db.init_app(AdMatch_app) # Initialize the database
    print("App initialized")
    return AdMatch_app

app = init_app()
from backend.controllers import *

if __name__ == "__main__":
    app.run()