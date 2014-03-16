from flask import Flask,url_for,request,render_template
app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('login.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if len(request.form["username"]) < 8 or len(request.form["password"]) < 8:
            error = "username or password is invalid"
        else:
            error = "login success"
    else:
        return 'error not support get request'
    return render_template('regut.html',error=error)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug = True)
