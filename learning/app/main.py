# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/parm/<parm>')
def withParm(parm):
  #python 2,7 still does not support f strings
  #return 'parm: %s' % escape(parm)
  #with format
  return 'parm: {}'.format(escape(parm))

@app.route('/int/<int:parm>') # if not int return 404
def withParmType(parm):
  return 'int: %s' % parm