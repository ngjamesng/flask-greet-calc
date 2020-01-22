# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>home page </h1>"


@app.route("/add")
def addition():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    result = add(a, b)
    return f"<h1>adding: {result}</h1>"

@app.route("/sub")
def subtraction():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    result = sub(a, b)
    return f"<h1>subtracting: {result}</h1>"

@app.route("/mult")
def multiply():
    a = int(request.args.get("a", 1))
    b = int(request.args.get("b", 1))
    result = mult(a, b)
    return f"<h1>Multiplying {result}</h1>"

@app.route("/div")
def divide():
    a = int(request.args.get("a", 1))
    b = int(request.args.get("b", 1))
    result = div(a, b)
    return f"<h1>dividing {result}</h1>"