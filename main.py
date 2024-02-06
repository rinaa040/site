from flask import Flask

app = Flask(__name__)
@app.route("/")
@app.route("/image_mars")
def index():
    with open("index.html", "r", encoding="utf") as f:
        return f.read()
@app.route('/index')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                    <link rel="stylesheet" type="text/css" href="static/css/style.css" />
                  </head>
                  <body>
                    <h1>И на Марсе будут яблони цвести!</h1>
                  </body>
                </html>"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)