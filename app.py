import os

from flask import Flask, render_template, session, request, flash

app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Andela Room Allocator"

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello sir!"


# @app.route('/login', methods=['POST'])
# def do_admin_login():
#     if request.form['password'] == 'password' and request.form['username'] == 'admin':
#         session['logged_in'] = True
#     else:
#         flash('Wrong password!')
#         return home()


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
