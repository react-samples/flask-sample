from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8"/>
            <link rel="stylesheet" href="/static/style.css"/>
          </head>
          <body>
            <h1>Hello World</h1>
          </body>
        </html>
    """
