#-*- coding:utf-8 -*-
from funtyping import app
from flask import render_template,request,flash,redirect,url_for
from funtyping.mail.mail import *
from funtyping.models.user_models import *
import random,string,os

@app.route('/')
def index():
    return render_template('regist.html')

@app.route('/regist',methods=['GET', 'POST'])
def regist():
    return render_template('regist.html') 
def get_user_id():
    pass

@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        toaddrs = request.form['email']
        code = string.join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890',20)).replace(' ','')
        emails = User_regist.query.filter_by(email=toaddrs).first()
        if not emails:
            add_user_regist(toaddrs,code)
            mailregist(toaddrs,app.config['MAILUN'],app.config['MAILPW'],code)
            return render_template('password.html',email=toaddrs)
        else:
            flash(u'用户已存在')
    return redirect(url_for('regist'))

app.secret_key = os.urandom(24)

@app.route('/init-password', methods=['GET','POST'])
def password():
    if request.method == 'POST':
        toaddrs = request.form['email']
        username = request.form['email']
        password = request.form['password']
        status = request.form['status']
        salt = string.join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890',5)).replace(' ','')
        if toaddrs and len(password)>5:
            add_user(salt,toaddrs,username,password,status)
            return render_template('login.html',email=toaddrs)
    elif request.method == 'GET':
        useremail = request.args.get('email','')
        usercode = request.args.get('code','')
        uemail = User.query.filter_by(email=useremail).first()
        ucodedb = User_regist.query.filter_by(email=useremail).first()
        ucode = ucodedb.code
        if uemail and ucode == usercode :
            update_status(useremail)
            return render_template('login.html',email=useremail)
        else:
            return render_template('password.html',email=useremail,status='1')

    return ''

