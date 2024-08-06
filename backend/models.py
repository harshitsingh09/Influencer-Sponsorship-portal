from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Instance of SQLAlchemy

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False, default='1')
    lists = db.relationship('List', backref='user', lazy=True)

class List(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cards = db.relationship('Card', backref='list', lazy=True)
    
class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    last_updated_date = db.Column(db.Date, nullable=False)
    deadline_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(100), nullable=False, default='0')
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)

# class Sponsor(db.Model):
#     __tablename__ = 'sponsor'  # Table name
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     role = db.Column(db.String(100), nullable=False, default='2')
#     industry = db.Column(db.String(100), nullable=False)
#     budget = db.Column(db.Integer, nullable=False)

# class Influencer(db.Model):
#     __tablename__ = 'influencer'  # Table name
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     role = db.Column(db.String(100), nullable=False, default='3')
#     reach = db.Column(db.Integer, nullable=False)
#     niche = db.Column(db.String(100), nullable=False)
