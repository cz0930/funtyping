#-*- coding:utf-8 -*-
from funtyping import app
from flask import render_template,request,flash,redirect,url_for,session
from funtyping.models.user_models import *
import os
from funtyping.utils.util import get_user_id

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        uuser = User.query.filter_by(email=username).first()
        userpw = user_login(uuser.salt,password)
        if uuser.status == '1':
            if uuser.password == userpw and uuser.email == username:
                session['user_id'] = uuser.id
                return redirect(url_for('latest'))
            else:
                flash(u'用户名或密码错误')
                return redirect(url_for('login'))
        else:
            flash(u'请登录邮箱验证注册信息')
    return redirect(url_for('latest'))

app.secret_key = os.urandom(24)

@app.route('/logout')
def logout():
    if 'user_id' in session:
        del session['user_id']
    return redirect(url_for('login'))

@app.route('/setting/password',methods=['GET', 'POST'])
def setpasswd():
    if request.method == 'GET':
        return render_template('change_password.html')
    elif request.method == 'POST':
        if get_user_id():
            user_id = get_user_id()
            password = request.form['old']
            newpassword = request.form['new']
            print newpassword
            renewpassword = request.form['confirm']
            uuser = User.query.filter_by(id=user_id).first()
            if newpassword != renewpassword or newpassword =='':
                flash(u'两次输入的密码不一致')
                return redirect(url_for('setpasswd'))
            elif user_login(uuser.salt,password)==uuser.password:
                update_password(user_id,uuser.salt,newpassword)
                flash(u'密码修改完成')
            else:
                flash(u'当前密码输入错误')
                return redirect(url_for('setpasswd'))

    return redirect(url_for('login'))
