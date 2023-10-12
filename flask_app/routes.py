from flask_app import app

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/kontakt")
def contact():
    return "<h1>Kontakta oss!</h1>"

@app.route("/omoss")
def omoss():
    return "<h1>Python gänget!</h1>"

@app.route("/test")
def contact():
    return "<h1>Test!</h1>"