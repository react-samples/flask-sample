from flask import Flask
app = Flask(__name__)

@app.route('/hoge', methods=['GET'])
def hoge():
    return "hoge"

@app.route('/hoge', methods=['POST'])
def Hoge():
    return "Hoge"
