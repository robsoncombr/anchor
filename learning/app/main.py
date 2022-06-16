from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/<parm>')
def withParm(parm):
  #python 2,7 still does not support f strings
  return 'parm: %s' % escape(parm)