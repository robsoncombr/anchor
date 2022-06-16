# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask, url_for, abort, redirect, request, session
from markupsafe import escape

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
# used in session
# generate good secret keys: python -c 'import os; print(os.urandom(16))'
app.secret_key = b'\xc5Q\n\x06\x0fd\x8a\xb1\xe9\xa2\x86\xe9\xc2\x95\xf9\xcf'

"""
@app.route('/parm/<parm>')
def withParm(parm):
    # python 2,7 still does not support f strings
    # return 'parm: %s' % escape(parm)
    # with format
    return 'parm: {}'.format(escape(parm))

@app.route('/int/<int:parm>')  # if not int return 404
def withParmType(parm):
    return 'int: %s' % parm
"""


@app.route('/')
def index():
    if 'username' in session:
        app.logger.debug('user access: %s', session['username'])
        return '''
          Logged in as %s
          <br><br>
          <a href="/logout">
            <input type="button" value="Logout" />
          </a>
      ''' % escape(session['username'])
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username'] or 'undefined'
        app.logger.debug('user login: %s', session['username'])
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <label for="username">Username:</label>
            <p><input type=text name=username>
            <p>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    if 'username' in session:
        app.logger.debug('user logout: %s', session['username'])
        #del session['username']
        session.pop('username', None)
    return redirect(url_for('index'))