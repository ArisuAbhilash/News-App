
import flask
from flask import render_template


app = flask.app("_name_")

@app.route("/")

def home ():
    return("index.html")
if __name__ == "_main_":
    app.run(debug=True)

