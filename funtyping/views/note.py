#-*- coding:utf-8 -*-
from funtyping import app
from flask import render_template,request,flash,redirect,url_for,session,escape
from funtyping.models.user_models import *
import datetime

@app.route('/')
def index():
    return render_template('regist.html')

@app.route('/write',methods=['GET','POST'])
def write():
    if request.method == 'GET':
        return render_template('write.html')
    elif request.method == 'POST':
        note_date = request.form["note_date"]
        note_content = request.form["note_content"]
        note_date = datetime.datetime.strptime(note_date, '%Y-%m-%d')
        if 'user_id' in session:
            user_id = escape(session['user_id'])
            write_note(user_id,note_date,note_content)
        else:
            return render_template('login.html') 
    return render_template('write.html') 
