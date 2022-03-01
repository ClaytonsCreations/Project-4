from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("templates/index.html")

@app.route("/team")
def team():
    return render_template("templates/team.html")

@app.route("/data")
def data():
    return render_template("templates/data.html")

@app.route("/ML")
def ML():
    return render_template("templates/machineLearning.html")

@app.route("/process")
def process():
    return render_template("templates/process.html")

@app.route("/analysis")
def analysis():
    return render_template("templates/analysis.html")

if __name__ == "__main__":
    app.run(debug=True)