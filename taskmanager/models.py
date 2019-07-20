from taskmanager.context import db, app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import json;
import os

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return 'User %' % self.email
        

class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, ForeignKey("user.id"))
    assigneeId = db.Column(db.Integer, ForeignKey("user.id"))
    assignment = db.Column(db.String(255))
    createdTS = db.Column(db.DateTime(True))
    completedTS = db.Column(db.DateTime(True))
    isComplete = db.Column(db.Boolean)
    
    def __repr__(self):
        return 'Task:[{0}] id:[{1}]'.format(self.assignment, self.id)