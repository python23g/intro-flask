from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Welcome!</h1>"

@app.route("/news/")
def news():
    return "<h1>News!</h1>"

@app.route("/home/")
def home():
    return "<h1>Home!</h1>"

@app.route("/about/")
def about():
    return "<h1>About!</h1>"


if __name__ == "__main__":
    app.run()
    