from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Instance of SQLAlchemy

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False, default=1)

# class Sponsor(db.Model):
#     __tablename__ = 'sponsor' # Table name
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     role = db.Column(db.String(100), nullable=False, default=2)
#     industry = db.Column(db.String(100), nullable=False)
#     budget = db.Column(db.Integer, nullable=False)

# class Influencer(db.Model):
#     __tablename__ = 'influencer' # Table name
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     role = db.Column(db.String(100), nullable=False, default=3)
#     reach = db.Column(db.Integer, nullable=False)
#     niche = db.Column(db.String(100), nullable=False)
