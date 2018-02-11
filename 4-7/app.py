from flask import Flask, render_template
from random import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', random=random())
