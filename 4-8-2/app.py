from flask import Flask, render_template
from random import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', l=[{"name": "Hoge", "value": "1"}, {"name": "Fuga", "value": "2"}, {"name": "Foo", "value": "3"}])
