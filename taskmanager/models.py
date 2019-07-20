from taskmanager.app import db, app
import json;
import os

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return 'User %' % self.email
        