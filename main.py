from flask import Flask, render_template
from variables import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", tempo=tempo)

@app.route("/vinicius")
def vinicius():
    return render_template("vinicius.html")

if __name__ == '__main__':
    app.run()
