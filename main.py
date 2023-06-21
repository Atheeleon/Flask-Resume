from flask import Flask, render_template
import datetime

def tempo():
    start_date = datetime.datetime(2021, 8, 24)
    end_date = datetime.datetime.now()

    duration = end_date - start_date

    years = duration.days // 365
    months = (duration.days % 365) // 30

    return f"{years} ano{'s' if years != 1 else ''} {f'''e {months} {'mês' if months == 1 else 'meses' }''' if months != 0 else ''}"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", tempo=tempo())

if __name__ == '__main__':
    app.run(host="0.0.0.0")