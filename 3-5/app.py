from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hoge')
def hoge():
    return 'hoge!'

@app.route('/foo/')
def foo():
    return 'foo'

@app.route('/fuga')
def fuga():
    return 'fuga'
