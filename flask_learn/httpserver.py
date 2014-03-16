from flask import Flask,url_for,request,render_template,make_response,abort,redirect,escape,session
app = Flask(__name__)

@app.route('/send_cookie',methods=['GET', 'POST'])
def send_cookie():
    resp = make_response(render_template('login.html'))
    resp.set_cookie('username','kingsley')
    return resp

@app.route('/recv_cookie',methods=['GET', 'POST'])
def recv_cookie():
    username = request.cookies.get('username')
    return username

#@app.route('/')
#def index():
#    return redirect(url_for('login'))

#@app.route('/login')
#def login():
#    abort(401)
#    this_is_never_executed()

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''<form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
            </form>'''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug = True)
