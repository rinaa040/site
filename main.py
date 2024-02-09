from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route('/index/<title>')
def index(title):
    return render_template("base.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template("trainings.html", prof=prof)


@app.route('/list_prof/<lst>')
def list_prof(lst):
    return render_template("professions.html", list=lst)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
