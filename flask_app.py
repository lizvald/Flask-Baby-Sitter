
# A very simple Flask Hello World app for you to get started with...
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello!'

@app.route('/science')
def hello_science():
    return 'I Love Science!'

@app.route('/', methods=["GET"])
def index():
    return render_template("main_page.html")

git init