from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer)
    username = db.Column(db.String(40), unique=True, primary_key=True)

    chat = db.relationship('Chats', back_populates='user')

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username
        }


class Chats(db.Model):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True)
    user1_username = db.Column(db.String(40), db.ForeignKey('users.username'))
    user2_username = db.Column(db.String(40), db.ForeignKey('users.username'))
    writer_username = db.Column(db.String(40))
    message = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('Users', back_populates='chat')
    

    def __repr__(self):
        return '<Chat %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user1_username": self.user1_username,
            "user2_username": self.user2_username,
            "writer_username": self.writer_username,
            "message": self.message,
            "created_at": self.created_at
        }


# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }