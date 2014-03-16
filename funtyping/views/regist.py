from funtyping import app
from flask import render_template,request
from funtyping.mail.mail import *

@app.route('/regist',methods=['GET', 'POST'])
def regist():
    return render_template('regist.html') 
def get_user_id():
    pass

@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        toaddrs = request.form['email']
        mailregist(toaddrs)
    return 'OK'

