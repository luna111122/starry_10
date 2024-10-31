from main import db
from datetime import datetime
class Diary(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(200), nullable=False)
    content=db.Column(db.Text(), nullable=False)
    emotion = db.Column(db.String(10), nullable=False)
    distract = db.Column(db.String(10), nullable=False)
    todo= db.Column(db.String(10), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Highlight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)

class goals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    day=db.Column(db.Text(),nullable=True)




class Monday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    highlight = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(1), nullable=True)

class Tuesday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    highlight = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(1), nullable=True)

class Wednesday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    highlight = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(1), nullable=True)


class Thursday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    highlight = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(1), nullable=True)

class Friday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)
    highlight = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(1), nullable=True)



