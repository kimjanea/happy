from flask import Flask
app = Flask(__name__)

@app.route("/root")
def root():
    return "hello flask"

@app.route("/greet")
def greet(name):
	return "Hello" + name
