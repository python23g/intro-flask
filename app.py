from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Welcome!</h1>"

@app.route("/news/")
def news():
    return "<h1>News!</h1>"

@app.route("/index/")
@app.route("/home/")
def home():
    return "<h1>Home!</h1>"

@app.route("/contact/")
@app.route("/about/")
def about():
    return "<h1>Contact!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
