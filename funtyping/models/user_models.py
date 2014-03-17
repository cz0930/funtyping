#-*- coding:utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from funtyping import app
import hashlib

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost/funtyping'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    salt = db.Column(db.String(15))
    username = db.Column(db.String(30))
    password = db.Column(db.String(40))
    email = db.Column(db.String(63))
    status = db.Column(db.String(1))
    create_time = db.Column(db.DateTime)
    def __init__(self,salt,username,password,email,status):
        self.salt= salt
        self.username = username
        self.password = password
        self.email = email
        self.status = status
    def __repr__(self):
        return self.id,self.password,self.status,self.salt

class User_regist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(63))
    code = db.Column(db.String(150))
    create_time = db.Column(db.DateTime)

    def __init__(self, email,code):
        self.email = email
        self.code = code
    def __repr__(self):
        return  self.code

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    content = db.Column(db.Text)

    def __init__(self,user_id,time,update_time,content):
        self.user_id = user_id
        self.time = time
        self.update_time = update_time
        self.content = content
    def __repr__(self):
        return self.user_id,self.time,self.update_time,self.content

def add_user_regist(email,code):
    addmail = User_regist(email,code)
    db.session.add(addmail)
    db.session.commit()

def add_user(salt,email,username,password,status):
    passw = hashlib.sha1(salt+password).hexdigest()
    adduser = User(salt,username,passw,email,status)
    db.session.add(adduser)
    db.session.commit()

def update_status(useremail):
    u = User.query.filter_by(email=useremail).first()
    u.status = '1'
    db.session.commit()

def user_login(salt,password):
    passw = hashlib.sha1(salt+password).hexdigest()
    return passw

def write_note(user_id,time,content):
    writenote = Note(user_id,time,'',content)
    db.session.add(writenote)
    db.session.commit()

