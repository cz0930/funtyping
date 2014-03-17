#-*- coding:utf-8 -*-
from funtyping import app
from flask import render_template,request,flash,redirect,url_for,session
from funtyping.models.user_models import *
import os

@app.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/loginer',methods=['GET', 'POST'])
def loginer():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        uuser = User.query.filter_by(email=username).first()
        userpw = user_login(uuser.salt,password)
        if uuser.status == '1':
            if uuser.password == userpw and uuser.email == username:
                session['user_id'] = uuser.id
                return redirect(url_for('write'))
            else:
                flash(u'用户名或密码错误')
                return redirect(url_for('login'))
        else:
            flash(u'请登录邮箱验证注册信息')
    return redirect(url_for('login'))
app.secret_key = os.urandom(24)

@app.route('/logout')
def logout():
    if 'user_id' in session:
        del session['user_id']
    return redirect(url_for('login'))
