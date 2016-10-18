@app.route("./root")
def root():
    return "hello flask"

@app.route("/greet/<name>")
def greet(name):
	name  = raw_input("Please Enter Your Name:	")
	return "Hello" + name
