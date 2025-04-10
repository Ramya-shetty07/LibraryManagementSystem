from .database import db

class User(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    username = db.Column(db.String(),nullable = False,unique = True)
    password = db.Column(db.String(),nullable = False)
    type = db.Column(db.String(),default = "general")
    bk = db.relationship("Book", backref = "creator")

class Book(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    book_title = db.Column(db.String(), nullable = False)
    author_name = db.Column(db.String(),nullable = False)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))