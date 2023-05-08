from flask import Flask, render_template
from variables import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", tempo=tempo)


if __name__ == '__main__':
    app.run()
