from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """homepage!!!"""
    return "<h1>homepage route</h1>"


@app.route("/welcome")
def welcome():
    """welcome page!!!"""
    return "<h1>welcome route</h1>"


@app.route("/welcome/home")
def welcome_home():
    """welcome home page!!!"""
    return "<h1>welcome Home route</h1>"


@app.route("/welcome/back")
def welcome_back():
    """welcome back page!!!"""
    return "<h1>welcome back route</h1>"
