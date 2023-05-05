from flask import Flask, render_template
from variables import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", tempo=tempo)

@app.route("/tcc")
def tcc():
    return render_template("tcc.html")


if __name__ == '__main__':
    app.run()
