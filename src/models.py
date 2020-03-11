from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Chats(db.Model):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    messages = db.relationship('Messages', back_populates='chat')
    invites = db.relationship('Invites', back_populates='post')
    
    
    def __repr__(self):
        return '<Chat %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "message": [a.serialize() for a in self.messages],
            "created_at": self.created_at
        }


class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'))
    writer_username = db.Column(db.String(40))
    message = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    chat = db.relationship('Chats', back_populates='messages')
    
    def __init__(self, chat_id, writer_username, message, created_at = datetime.utcnow()):
        chat = Chats.query.get( chat_id )
        if chat is None:
            raise Exception(f'Chat with id "{chat_id}" does not exist')
        invited_users = [x.username.lower().strip() for x in chat.invites]
        writer_username = writer_username.lower().strip()
        if invited_users != []:
            if writer_username not in invited_users:
                raise Exception(f'{writer_username} not invited to chat')
        
        self.chat_id = chat_id
        self.writer_username = writer_username
        self.message = message
        self.created_at = created_at

    def __repr__(self):
        return '<Message %r>' % self.id

    def serialize(self):
        return {
            "writer_username": self.writer_username,
            "message": self.message,
            "created_at": self.created_at
        }

class Invites(db.Model):
    __tablename__ = 'invites'
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'))
    username = db.Column(db.String(40))
    post = db.relationship('Chats', back_populates='invites')
    

    def __repr__(self):
        return '<Invite %r>' % self.id

    def serialize(self):
        return {
            "username": self.user_name
        }

    '''
class Users(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(80), primary_key=True)
    
    def serialize(self):
        return {
            "username": self.username
        }


class Chats(db.Model):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    messages = db.relationship('Messages', back_populates='chat')

    def serialize(self):
        return {
            "id": self.id,
            "message": [a.serialize() for a in self.messages],
            "created_at": self.created_at
        }


class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'))
    writer_username = db.Column(db.String(80), db.ForeignKey('users.username'))
    message = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    chat = db.relationship('Chats', back_populates='messages')
    
    def serialize(self):
        return {
            "id": self.id,
            "chat_id": self.chat_id,
            "writer_username": self.writer_username,
            "message": self.message,
            "created_at": self.created_at
        }
'''